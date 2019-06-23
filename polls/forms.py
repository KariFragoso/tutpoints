from django import forms
from .models import Question, Choice

class questionForm(forms.ModelForm):
	
	class Meta:
		model = Question
		fields = ('question_text',); 
		labels = {
            'question_text': 'Pergunta',
        }

class choiceForm(forms.ModelForm):
	
	class Meta:
		model = Choice
		fields = ('choice_text', 'votes', 'question');
		labels = {
            'choice_text': 'Opção',
            'votes': 'Numero de Votos',
            'question': 'Questão',
        }