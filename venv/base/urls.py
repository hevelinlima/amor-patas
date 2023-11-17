from django.urls import path
from . import views 

app_name = 'base'

urlpatterns = [
    path('', views.inicio, name='Amor&Patas'),
    path('contatos/', views.contatos, name='contactus'),
    path('lista_animais/', views.lista_animais, name="lista_animais")
]