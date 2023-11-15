from django.urls import path
from . import views 

app_name = 'animais'

urlpatterns = [
    path('registrar/', views.registro, name='registro'),
]