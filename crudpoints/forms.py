from django import forms
from .models import Funcionario
from .models import Ponto, Cargo



class FuncForm(forms.ModelForm):

    class Meta:
       model = Funcionario
       fields = ('nome', 'genero', 'dataNasc', 'rg', 'pis', 'funcao', 'data_admissao', 'cargaH', 'email'); 
       

class PontoForm(forms.ModelForm):

	class Meta(object):
		model = Ponto 
		fields = ('funcionario','horaEnt1', 'horaSaida1', 'horaEnt2', 'horaSaida2');

class CargoForm(forms.ModelForm):

	class Meta(object):
		model = Cargo
		fields = ('nomeCargo', 'departamento');

