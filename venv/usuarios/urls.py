from django.urls import path
from . import views 

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('validacao_cadastro/', views.validacao_cadastro, name='validacao_cadastro'),
    path('validacao_login/', views.validacao_login, name='validacao_login'),
    path('logout/', views.logout, name='logout'),
    path('inicio/', views.inicio, name='Amor&Patas')
]