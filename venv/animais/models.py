from django.db import models
from datetime import date
from django.core.validators import MinValueValidator

# Create your models here.
class Animais(models.Model):
  porte_choices = [
    ("Pequeno", "Pequeno"),
    ("Médio", "Médio"),
    ("Grande", "Grande"),
    ("Extra Grande", "Extra Grande"),
  ]
  vacinacao_choices = [
    ("Sim", "Sim"),
    ("Não", "Não")
  ]
  genero_choices = [
    ("Fêmea", "Fêmea"),
    ("Macho", "Macho")
  ]
  nome = models.CharField(max_length=100)
  especie = models.CharField(max_length=50)
  idade = models.IntegerField(validators=[MinValueValidator(0)], default=1)
  porte = models.CharField(max_length=12, choices=porte_choices, default="Pequeno")
  peso = models.IntegerField(validators=[MinValueValidator(0)], default=1)
  raça = models.CharField(max_length=50)
  origem = models.CharField(max_length=100)
  vacinacao_em_dia = models.CharField(max_length=3, choices=vacinacao_choices, default="Sim")
  genero = models.CharField(max_length=5, choices=genero_choices, default="Fêmea")
  
  class Meta: 
    verbose_name = "Registro de animais"
    verbose_name_plural = "Registros dos animais"
    ordering = ["nome"]