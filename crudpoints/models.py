from django.db import models
from django.utils import timezone
from datetime import datetime

class Cargo(models.Model):

    nomeCargo = models.CharField(max_length=50)
    departamento =  models.CharField(max_length=50)


    def __str__(self):
      return self.nomeCargo

class Funcionario(models.Model):
    
    nome = models.CharField(max_length= 200)
    funcao = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    dataNasc = models.DateField()
    cargaH = models.CharField(max_length=2)
    data_admissao = models.DateField(default=timezone.now)
    pis= models.CharField(max_length=11, default=" ")
    rg = models.CharField(max_length=8, default=" ")
    email = models.EmailField(max_length=100, default=" ")

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outros'),
    )
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES, default=" ")
    

    def __str__(self):
      return self.nome



class Ponto(models.Model):

    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data =  models.DateField(default=datetime.now())
    horaEnt1 = models.TimeField()
    horaSaida1 = models.TimeField()
    horaEnt2 =  models.TimeField()
    horaSaida2 = models.TimeField()

