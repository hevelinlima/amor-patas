from django.urls import path
from . import views 

app_name = 'animais'

urlpatterns = [
  path('cadastro_animais/', views.cadastro_animais, name='cadastro_animais'),
  path('cadastro_especies/', views.cadastro_especies, name='cadastro_especies'),
  path('cadastro_racas/', views.cadastro_racas, name='cadastro_racas'),
  path('cadastro_portes/', views.cadastro_portes, name='cadastro_portes'),
  path('cadastro_generos/', views.cadastro_generos, name='cadastro_generos'),
]