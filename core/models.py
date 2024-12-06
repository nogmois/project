from django.db import models

class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    ano = models.IntegerField()
    placa = models.CharField(max_length=10, unique=True)
    imagem = models.ImageField(upload_to='carros/', blank=True, null=True)  # Campo para imagem


    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"

class TipoServico(models.Model):
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.descricao

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome
