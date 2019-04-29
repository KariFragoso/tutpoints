from django.contrib import admin
from .models import Funcionario, Ponto, Cargo
from polls.models import Question, Choice

admin.site.register(Funcionario)
admin.site.register(Ponto)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Cargo)


# Register your models here.
