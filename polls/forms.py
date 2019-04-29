from django import forms
from .models import Question, Choice

class questionForm(forms.ModelForm):
	
	class Meta:
		model = Question
		fields = ('question_text',); 


class choiceForm(forms.ModelForm):
	
	class Meta:
		model = Choice
		fields = ('choice_text', 'votes', 'question'); 