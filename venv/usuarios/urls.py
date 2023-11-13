from django.urls import path
from . import views 

app_name = 'usuarios'

urlpatterns = [
    path('', views.usuarios, name='usuarios'),
    path('inicio/', views.inicio, name='Amor&Patas')
]