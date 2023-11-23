from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from animais.models import Animais
from base.forms import SolicitacaoAdocaoForm
from base.models import SolicitacaoAdocao

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
  


def solicitacao_adocao(request):
    if request.method == 'POST':
        form = SolicitacaoAdocaoForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return HttpResponse("Formulário enviado com sucesso")
    else:
        form = SolicitacaoAdocaoForm()

    return render(request, 'solicitacao_adocao.html', {'form': form})

"""def lista_solicitacoes(request):
    solicitacoes = Solicitacao.objects.all()
    return render(request, 'lista_solicitacoes.html', {'solicitacoes': solicitacoes})
"""

def verificar_status(request, solicitacao_id):
  solicitacao = get_object_or_404(SolicitacaoAdocao, pk=solicitacao_id)

  if request.user.is_authenticated and solicitacao.user == request.user:
    return render(request, 'verificar_status.html', {'solicitacao': solicitacao})
  else:
    return redirect('login')

def contatos(request):
  return render(request, 'contatos.html')