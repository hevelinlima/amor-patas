from django.shortcuts import render
from django.http import HttpResponse
from animais.models import Animais

# Create your views here.
def inicio(request):
  return render(request, 'inicio.html')

def lista_animais(request):
  animais = Animais.objects.all()
  
  return render(request, "lista_animais.html", {'animais': animais})

def card_animal(request, id):

  card = Animais.objects.get(id = id)

  return render(request, "card_animais.html", {'card': card})

def contatos(request):
  return render(request, 'contatos.html')