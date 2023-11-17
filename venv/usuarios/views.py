from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from django.urls import reverse 
from hashlib import sha256

# Create your views here.
def login(request):
  status = request.GET.get('status')
  return render(request,'login.html', {'status': status})

def cadastro(request):
  status = request.GET.get('status')
  return render(request,'cadastro.html', {'status': status})

def validacao_cadastro(request):
  nome = request.POST.get('nome')
  sobrenome = request.POST.get('sobrenome')
  email = request.POST.get('email')
  senha = request.POST.get('senha')

  usuario = Usuario.objects.filter(email = email)
  if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(sobrenome.strip()) == 0:
    return redirect(reverse('usuarios:cadastro') + '?status=1')
  
  if len(senha) < 8:
    return redirect(reverse('usuarios:cadastro') + '?status=2')

  if len(usuario) > 0:
    return redirect(reverse('usuarios:cadastro') + '?status=3')
  try:
    senha = sha256(senha.encode()).hexdigest()
    usuario = Usuario(nome=nome, sobrenome=sobrenome, email=email, senha=senha)
    usuario.save()

    return redirect(reverse('usuarios:cadastro') + '?status=0')
  except:
    return redirect(reverse('usuarios:cadastro') + '?status=4')
  
def validacao_login(request):
  email = request.POST.get('email')
  senha = request.POST.get('senha')
  senha = sha256(senha.encode()).hexdigest()

  usuario = Usuario.objects.filter(email = email).filter(senha = senha)
 
  if len(usuario) == 0:
    return redirect(reverse('usuarios:login') + '?status=1')
  elif len(usuario) > 0:
    request.session['usuario'] = usuario[0].id 
    return redirect(reverse('animais:registro'))

  return HttpResponse(f'{email}, {senha} ')

def logout(request):
  request.session.flush()
  return redirect(reverse('usuarios:login'))

  

  