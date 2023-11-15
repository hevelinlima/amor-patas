from django.urls import path
from . import views 

app_name = 'usuarios'

urlpatterns = [
    path('', views.usuarios, name='usuarios'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('validacao/', views.validacao, name='validacao'),
    path('inicio/', views.inicio, name='Amor&Patas')
]