from django.shortcuts import render
from animais.models import Animais

# Create your views here.
def inicio(request):
  return render(request, 'inicio.html')

def lista_animais(request):
  animais = Animais.objects.all()
  
  return render(request, "lista_animais.html", {'animais': animais})

def contatos(request):
  return render(request, 'contatos.html')