from django.shortcuts import render, get_object_or_404, redirect
from .models import Carro
from .forms import CarroForm
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db.models import Count
from io import BytesIO
import base64
from collections import Counter
import matplotlib
matplotlib.use('Agg')  # Use o backend sem interface gráfica
import matplotlib.pyplot as plt

def cadastrar_carro(request):
    if request.method == "POST":
        form = CarroForm(request.POST, request.FILES)  # Inclua request.FILES para lidar com imagens
        if form.is_valid():
            form.save()
            return redirect('listar_carros')  # Redirecione para a listagem de carros
    else:
        form = CarroForm()  # Inicialize um formulário vazio
    return render(request, 'core/cadastrar_carro.html', {'form': form, 'request': request})


def listar_carros(request):
    carros = Carro.objects.all()
    return render(request, 'core/listar_carros.html', {'carros': carros, 'request': request})


def editar_carro(request, pk):
    carro = get_object_or_404(Carro, pk=pk)
    if request.method == "POST":
        form = CarroForm(request.POST, request.FILES, instance=carro)  # Inclua request.FILES para imagens
        if form.is_valid():
            form.save()
            return redirect('listar_carros')  # Redirecione após salvar
    else:
        form = CarroForm(instance=carro)  # Inicialize o formulário com os dados existentes
    return render(request, 'core/editar_carro.html', {'form': form, 'request': request})


def excluir_carro(request, pk):
    carro = get_object_or_404(Carro, pk=pk)
    carro.delete()
    return redirect('listar_carros')


def gerar_relatorio_carros(request):
    # Obter dados dos carros
    carros = Carro.objects.all()

    # Contar carros por marca
    marcas = [carro.marca for carro in carros]
    marca_count = Counter(marcas)

    # Gerar gráfico de pizza
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(marca_count.values(), labels=marca_count.keys(), autopct='%1.1f%%', startangle=90)
    ax.set_title('Distribuição de Carros por Marca')

    # Salvar gráfico como imagem em base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')  # Adicionado bbox_inches para ajustar margens
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    plt.close(fig)  # Fecha o gráfico para evitar uso desnecessário de memória

    # Renderizar o HTML
    html_string = render_to_string('core/relatorio_carros.html', {
        'carros': carros,
        'grafico_base64': image_base64,  # Passar a imagem do gráfico como base64
        'request': request
    })

    # Gerar PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="relatorio_carros.pdf"'
    pisa_status = pisa.CreatePDF(html_string, dest=response)

    if pisa_status.err:
        return HttpResponse(f"Erro ao gerar PDF: {pisa_status.err}", status=500)

    return response



def estatisticas(request):
    total_carros = Carro.objects.count()
    por_marca = Carro.objects.values('marca').annotate(total=Count('marca'))
    return render(request, 'core/estatisticas.html', {
        'total_carros': total_carros,
        'por_marca': por_marca,
        'request': request,
    })
