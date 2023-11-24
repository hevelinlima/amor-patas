from django.shortcuts import render
from .models import Colaboradores
from .forms import ColaboradoresForm

# Create your views here.
def cadastro_colaboradores(request):
  sucesso = False   
  form = ColaboradoresForm(request.POST or None, request.FILES or None)
  if form.is_valid(): 
      sucesso = True
      form.save()
  contexto = {
      'form':form,
      'sucesso': sucesso
    }
  return render(request, 'cadastro_colaboradores.html', contexto)

def lista_colaboradores(request):
   colaboradores = Colaboradores.objects.all()

   return render(request, "lista_colaboradores.html", {'colaboradores': colaboradores})