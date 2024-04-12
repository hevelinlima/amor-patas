from django.db import models
from django.forms import CharField
from django.core.validators import MinValueValidator

# Create your models here.
class Colaboradores(models.Model):
  cargo_choices = [
    ("Cuidador", "Cuidador"),
    ("Voluntário", "Voluntário")
  ]
  nome_completo = models.CharField(max_length=100)
  endereço_residencial = models.CharField(max_length=255)
  endereço_de_email = models.EmailField()
  numero_de_telefone = models.IntegerField(validators=[MinValueValidator(0)], default=(86))
  cargo = models.CharField(max_length=10, choices=cargo_choices, default="Cuidador")
  formaçao_ou_certificações = models.TextField(blank=True, null=True)
  restriçoes_ou_condiçoes_de_saude = models.CharField(max_length=255, default='Nenhuma')
  contato_de_emergencia = models.IntegerField(validators=[MinValueValidator(0)], default=(86))
  nome_do_contato_de_emergencia = models.CharField(max_length=100)
  foto = models.ImageField(upload_to='MEDIA_URL', blank=True, null=True)

  def __str__(self) -> str:
    return self.nome_completo
  
  class Meta: 
    verbose_name = "Formulário de colaborador"
    verbose_name_plural = "Formulários dos colaboradores"
    ordering = ["nome_completo"]




