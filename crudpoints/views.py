from django.shortcuts import render
from .models import Funcionario, Ponto, Cargo
from django.utils import timezone
from .forms import FuncForm, PontoForm, CargoForm
from polls.models import Choice, Question
import operator
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def telainicial(request):
	questions = Question.objects.all()
	pergunta = questions[questions.count()-1]
	esc = Choice.objects.all().filter(question=questions[questions.count()-1])
	ordered = sorted(esc, key=operator.attrgetter('votes'), reverse = True)
	first = ordered[0]

	funcionarios = Funcionario.objects.all()
	return render(request, 'crudpoints/layout.html', {'funcionarios':funcionarios, 'resultado':first, 'pergunta':pergunta})

def editarperfil(request):
	return render(request, 'crudpoints/editprofile.html', {})

def newfunc(request):
	if request.method == "POST":
		form = FuncForm(request.POST)
		if form.is_valid():
			funcionario = form.save(commit=False)
			funcionario.save()
	else:
		form = FuncForm()

	return render(request, 'crudpoints/editFunc.html', {'form': form})


def listafunc(request):
	funcionarios = Funcionario.objects.all()
	return render(request, 'crudpoints/list.html', {'funcionarios': funcionarios})

def editfunc(request, pk):
	funcionario = get_object_or_404(Funcionario, pk=pk)
	if request.method == "POST":
		form = FuncForm(request.POST, instance=funcionario)
		if form.is_valid():
			funcionario = form.save(commit=False)
			funcionario.save()
			return redirect('listafunc')
	else:
		form = FuncForm(instance=funcionario)
	return render(request, 'crudpoints/editFunc.html', {'form': form})

def deletefunc(request,pk):
	funcionario = get_object_or_404(Funcionario, pk=pk)
	funcionario.delete()
	return redirect('listafunc')

def pontonew(request):
	
	if request.method == "POST":
		form = PontoForm(request.POST)
		if form.is_valid():
			ponto = form.save(commit=False)
			ponto.save()
	else:
		form = PontoForm()

	return render(request, 'crudpoints/pontonew.html', {'form': form})

def relatoriogeral(request):
	pontos = Ponto.objects.all()
	return render(request, 'crudpoints/relatorio.html', {'pontos':pontos})




def relatorioespecifico(request,pk):
	pontos = Ponto.objects.filter(funcionario_id=pk)
	for ponto in pontos:
		print("")
	return render(request, 'crudpoints/relatorio.html', {'pontos':pontos})

def morefunc(request,pk):
	funcionario = get_object_or_404(Funcionario, pk=pk)
	return render(request, 'crudpoints/morefunc.html', {'funcionario': funcionario})



def newcargo(request):
	if request.method == "POST":
		form = CargoForm(request.POST)
		if form.is_valid():
			cargo= form.save(commit=False)
			cargo.save()
	else:
		form = CargoForm()

	return render(request, 'crudpoints/editCargo.html', {'form': form})


def listacargo(request):
	cargos = Cargo.objects.all()
	return render(request, 'crudpoints/listaCargo.html', {'cargos': cargos})

def editcargo(request, pk):
	cargo = get_object_or_404(Cargo, pk=pk)
	if request.method == "POST":
		form = CargoForm(request.POST, instance=cargo)
		if form.is_valid():
			cargo = form.save(commit=False)
			cargo.save()
			return redirect('listacargo')
	else:
		form = CargoForm(instance=cargo)
	return render(request, 'crudpoints/editCargo.html', {'form': form})

def deletecargo(request,pk):
	cargo = get_object_or_404(Cargo, pk=pk)
	cargo.delete()
	return redirect('listacargo')