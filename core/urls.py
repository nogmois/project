from django.urls import path
from . import views

urlpatterns = [
    path('carros/cadastrar/', views.cadastrar_carro, name='cadastrar_carro'),
    path('carros/', views.listar_carros, name='listar_carros'),
    path('carros/<int:pk>/editar/', views.editar_carro, name='editar_carro'),
    path('carros/<int:pk>/excluir/', views.excluir_carro, name='excluir_carro'),
    path('carros/relatorio/', views.gerar_relatorio_carros, name='relatorio_carros'),
    path('estatisticas/', views.estatisticas, name='estatisticas'),

]
