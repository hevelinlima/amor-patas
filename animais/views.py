from django.shortcuts import render
from animais.models import Animais
from animais.forms import AnimaisForm, EspeciesForm, RacasForm, PortesForm, GenerosForm
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
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

@user_passes_test(is_admin)
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

@user_passes_test(is_admin)
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

@user_passes_test(is_admin)
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

@user_passes_test(is_admin)
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
