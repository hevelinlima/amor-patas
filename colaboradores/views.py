from django.shortcuts import render
from .models import Colaboradores
from .forms import ColaboradoresForm
from django.contrib.auth.decorators import user_passes_test


def is_admin(user):
    return user.is_authenticated and user.is_staff

# Create your views here.
@user_passes_test(is_admin)
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