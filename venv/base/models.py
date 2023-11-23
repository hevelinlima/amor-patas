from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


# Create your models here.
class SolicitacaoAdocao(models.Model):
  residencia_choices = [
    ("Apartamento", "Apartamento"),
    ("Casa", "Casa")
  ]
  propriedade_choices = [
    ("Própria", "Própria"),
    ("Alugada", "Alugada")
  ]
  status_choices = [
    ('Pendente', 'Pendente'),
    ('Aceita', 'Aceita'),
    ('Recusada', 'Recusada'),
  ]
  user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
  nome_completo = models.CharField(max_length=100)
  endereço_residencial = models.CharField(max_length=255)
  endereço_email = models.EmailField()
  numero_de_telefone = models.IntegerField(validators=[MinValueValidator(0)], default=1)
  tipo_de_residencia = models.CharField(max_length=12, choices=residencia_choices, default="Casa")
  tipo_de_propriedade = models.CharField(max_length=8, choices=propriedade_choices, default="Própria")
  permissao_para_animais_no_local = models.BooleanField(default=False)
  motivacao_para_adotar = models.TextField() 
  o_que_espera_da_adocao = models.TextField()
  status = models.CharField(max_length=20, choices=status_choices, default='Pendente')

  class Meta: 
    verbose_name = "Formulário de adoção"
    verbose_name_plural = "Formulários de adoção"
    ordering = ["nome_completo"]
