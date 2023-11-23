from django.shortcuts import render
from animais.models import Animais
from animais.forms import AnimaisForm

def cadastro_animais(request):
  sucesso = False   
  form = AnimaisForm(request.POST or None)
  if form.is_valid(): 
      sucesso = True
      form.save()
  contexto = {
      'form':form,
      'sucesso': sucesso
    }
  return render(request, 'cadastro_animais.html', contexto)

