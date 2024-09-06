from django.db import models

# Create your models here.
class Grupo(models.Model):
    nome = models.CharField(max_length = 100)

    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=50)
    data_nascimento = models.DateField(max_length=20)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
