from django.urls import path
from . import views 

app_name = 'base'

urlpatterns = [
    path('', views.inicio, name='Amor&Patas'),
    path('contatos/', views.contatos, name='contactus'),
    path('lista_animais/', views.lista_animais, name="lista_animais"),
    path('card_animal/<int:id>', views.card_animal, name="card_animal"),
    path('search_animais/', views.search_animais, name="search_animais"),
    path('solicitacao_adocao/', views.solicitacao_adocao, name='solicitacao_adocao'),
     path('verificar_status/<int:solicitacao_id>/', views.verificar_status, name='verificar_status'),
]

    