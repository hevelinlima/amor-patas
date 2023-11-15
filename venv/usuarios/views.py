from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario

# Create your views here.
def inicio(request):
  return render(request, 'inicio.html')

def usuarios(request):
  return render(request,'usuarios.html')

def login(request):
  return HttpResponse('login')

def cadastro(request):
  return render(request,'cadastro.html')

def validacao(request):
  nome = request.POST.get('nome')
  sobrenome = request.POST.get('sobrenome')
  email = request.POST.get('email')
  senha = request.POST.get('senha')

  usuario = Usuario(nome=nome, sobrenome=sobrenome, email=email, senha=senha)
  usuario.save()

  return HttpResponse(f'{nome} {sobrenome}, {email}, {senha}')