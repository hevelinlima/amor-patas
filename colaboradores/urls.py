from django.urls import path
from . import views 

app_name = 'colaboradores'

urlpatterns = [
  path('cadastro_colaboradores/', views.cadastro_colaboradores, name='cadastro_colaboradores'),
  path('lista_colaboradores/', views.lista_colaboradores, name='lista_colaboradores'),
]