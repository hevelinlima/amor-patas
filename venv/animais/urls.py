from django.urls import path
from . import views 

app_name = 'animais'

urlpatterns = [
  path('cadastro_animais/', views.cadastro_animais, name='cadastro_animais')
]