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
		labels ={'funcionario' : 'Funcionário',
				'horaEnt1' : 'Hora de Entrada 1',
				'horaSaida1' : 'Hora de Saída 1', 
				'horaEnt2' : 'Hora de Entrada 2', 
				'horaSaida2' : 'Hora de Saída 2',
				}

class CargoForm(forms.ModelForm):

	class Meta(object):
		model = Cargo
		fields = ('nomeCargo', 'departamento');

