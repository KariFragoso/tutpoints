from .models import Funcionario, Ponto, Cargo
from django.utils import timezone
from .forms import FuncForm, PontoForm, CargoForm, ContatoForm, SignUpForm
from polls.models import Choice, Question
import operator
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



# Create your views here.
def telainicial(request):
	questions = Question.objects.all()
	pergunta = questions[questions.count()-1]
	esc = Choice.objects.all().filter(question=questions[questions.count()-1])
	ordered = sorted(esc, key=operator.attrgetter('votes'), reverse = True)
	first = ordered[0]

	funcionarios = Funcionario.objects.all()
	return render(request, 'crudpoints/layout.html', {'funcionarios':funcionarios, 'resultado':first, 'pergunta':pergunta})


@login_required
def editarperfil(request):
	return render(request, 'crudpoints/editprofile.html', {})

@login_required
def newfunc(request):
	if request.method == "POST":
		form = FuncForm(request.POST)
		if form.is_valid():
			funcionario = form.save(commit=False)
			funcionario.save()
			messages.success(request, 'Funcionário salvo com sucesso!')
	else:
		form = FuncForm()

	return render(request, 'crudpoints/editFunc.html', {'form': form})

@login_required
def listafunc(request):
	funcionarios = Funcionario.objects.all()
	return render(request, 'crudpoints/list.html', {'funcionarios': funcionarios})

@login_required
def editfunc(request, pk):
	funcionario = get_object_or_404(Funcionario, pk=pk)
	if request.method == "POST":
		form = FuncForm(request.POST, instance=funcionario)
		if form.is_valid():
			funcionario = form.save(commit=False)
			funcionario.save()
			messages.success(request, 'Funcionário salvo com sucesso!')
			return redirect('listafunc')
	else:
		form = FuncForm(instance=funcionario)
	return render(request, 'crudpoints/editFunc.html', {'form': form})

@login_required
def deletefunc(request,pk):
	funcionario = get_object_or_404(Funcionario, pk=pk)
	funcionario.delete()
	messages.success(request, 'Funcionário deletado com sucesso!')
	return redirect('listafunc')

@login_required
def pontonew(request):
	
	if request.method == "POST":
		form = PontoForm(request.POST)
		if form.is_valid():
			ponto = form.save(commit=False)
			ponto.save()
			messages.success(request, 'O Novo Horário Ponto foi salvo com sucesso!')
	else:
		form = PontoForm()

	return render(request, 'crudpoints/pontonew.html', {'form': form})

@login_required
def relatoriogeral(request):
	pontos = Ponto.objects.all()
	return render(request, 'crudpoints/relatorio.html', {'pontos':pontos})



@login_required
def relatorioespecifico(request,pk):
	pontos = Ponto.objects.filter(funcionario_id=pk)
	for ponto in pontos:
		print("")
	return render(request, 'crudpoints/relatorio.html', {'pontos':pontos})

@login_required
def morefunc(request,pk):
	funcionario = get_object_or_404(Funcionario, pk=pk)
	messages.success(request, 'O Novo funcionário salvo com sucesso!')
	return render(request, 'crudpoints/morefunc.html', {'funcionario': funcionario})


@login_required
def newcargo(request):
	if request.method == "POST":
		form = CargoForm(request.POST)
		if form.is_valid():
			cargo= form.save(commit=False)
			cargo.save()
			messages.success(request, 'O cargo foi salvo com sucesso!')  # <-
	else:
		form = CargoForm()

	return render(request, 'crudpoints/editCargo.html', {'form': form})

@login_required
def listacargo(request):
	cargos = Cargo.objects.all()
	return render(request, 'crudpoints/listaCargo.html', {'cargos': cargos})

@login_required
def editcargo(request, pk):
	cargo = get_object_or_404(Cargo, pk=pk)
	if request.method == "POST":
		form = CargoForm(request.POST, instance=cargo)
		if form.is_valid():
			cargo = form.save(commit=False)
			cargo.save()
			messages.success(request, 'O cargo foi editado com sucesso!')
			return redirect('listacargo')

	else:
		form = CargoForm(instance=cargo)
	return render(request, 'crudpoints/editCargo.html', {'form': form})

@login_required
def deletecargo(request,pk):
	cargo = get_object_or_404(Cargo, pk=pk)
	cargo.delete()
	return redirect('listacargo')

def contato(request):
    if request.method == 'GET':
        email_form = ContatoForm()
    else:
        email_form = ContatoForm(request.POST)
        if email_form.is_valid():
            emissor = email_form.cleaned_data['emissor']
            assunto = email_form.cleaned_data['assunto']
            msg = email_form.cleaned_data['msg']
            msg = msg+' Enviado por: '+emissor
            try:
                send_mail(assunto, msg, emissor, ['karileti.fragoso0@gmail.com'])
            except BadHeaderError:
                return HttpResponse("Erro =/")
            return redirect('obg')
    return render(request, 'crudpoints/contato.html', {'form': email_form})

def obg(request):
	return render(request, 'crudpoints/obg.html', {})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('telainicial')
    else:
        form = SignUpForm()
    return render(request, 'crudpoints/signup.html', {'form': form})

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

