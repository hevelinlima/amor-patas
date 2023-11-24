from django.shortcuts import render
from animais.models import Animais
from animais.forms import AnimaisForm, EspeciesForm, RacasForm, PortesForm, GenerosForm

def cadastro_animais(request):
  sucesso = False   
  form = AnimaisForm(request.POST or None, request.FILES or None)
  if form.is_valid(): 
      sucesso = True
      form.save()
  contexto = {
      'form':form,
      'sucesso': sucesso
    }
  return render(request, 'cadastro_animais.html', contexto)

def cadastro_especies(request):
  sucesso = False   
  form = EspeciesForm(request.POST or None)
  if form.is_valid(): 
      sucesso = True
      form.save()
  contexto = {
      'form':form,
      'sucesso': sucesso
    }
  return render(request, 'cadastro_especies.html', contexto)

def cadastro_racas(request):
  sucesso = False   
  form = RacasForm(request.POST or None)
  if form.is_valid(): 
      sucesso = True
      form.save()
  contexto = {
      'form':form,
      'sucesso': sucesso
    }
  return render(request, 'cadastro_racas.html', contexto)

def cadastro_portes(request):
  sucesso = False   
  form = PortesForm(request.POST or None)
  if form.is_valid(): 
      sucesso = True
      form.save()
  contexto = {
      'form':form,
      'sucesso': sucesso
    }
  return render(request, 'cadastro_portes.html', contexto)

def cadastro_generos(request):
  sucesso = False   
  form = GenerosForm(request.POST or None)
  if form.is_valid(): 
      sucesso = True
      form.save()
  contexto = {
      'form':form,
      'sucesso': sucesso
    }
  return render(request, 'cadastro_generos.html', contexto)
