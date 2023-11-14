from django.urls import path
from . import views 

app_name = 'animais'

urlpatterns = [
    path('cadastrar/', views.registro, name='registro'),
]