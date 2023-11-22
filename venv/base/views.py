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

def search_animais(request):
  if request.method == "POST":
    pesquisa = request.POST['pesquisa']
    animais_especie = Animais.objects.filter(especie__especie__contains=pesquisa)
    animais_raca = Animais.objects.filter(raça__raca__contains=pesquisa)
    animais_porte = Animais.objects.filter(porte__tipo__contains=pesquisa)
    animais_genero = Animais.objects.filter(genero__genero__contains=pesquisa)

    animais = animais_especie | animais_raca | animais_porte | animais_genero
    return render(request, 'search_animais.html', {'pesquisa': pesquisa, 'animais': animais})
  else:
    return render(request,'search_animais.html')

def contatos(request):
  return render(request, 'contatos.html')