from django import forms
from .models import Funcionario
from .models import Ponto, Cargo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row, Column, Reset




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


class ContatoForm(forms.Form):
    emissor = forms.EmailField(required=True, label='Remetente')
    assunto = forms.CharField(required=True)
    msg = forms.CharField(widget=forms.Textarea, label='Mensagem')


    def __init__(self, *args, **kwargs):
        super(ContatoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('emissor', css_class='form-group col-md-6'),
                Column('assunto', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            'msg'
        )
        self.helper.add_input(Submit('submit', 'Enviar'))
        self.helper.add_input(Reset('reset', 'Limpar', css_class='btn-danger float-right'))
