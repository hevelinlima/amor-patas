from django.db import models
from django.core.validators import MinValueValidator

class Especies(models.Model):
  especie = models.CharField(max_length=30)
  nome_cientifico = models.CharField(max_length=30)
  descricao = models.TextField() 

  def __str__(self) -> str:
    return self.especie
  
  class Meta: 
    verbose_name = "Espécie"
    ordering = ["especie"]
  
class Porte(models.Model):
  tipo = models.CharField(max_length=30)
  descrição = models.TextField()

  def __str__(self) -> str:
    return self.tipo
  
class Raca(models.Model):
  raca = models.CharField(max_length=30)
  descricao = models.TextField() 
  especie = models.ForeignKey(Especies, on_delete=models.DO_NOTHING)

  def __str__(self) -> str:
    return self.raca
  
class Genero(models.Model):
  genero = models.CharField(max_length=30)
  descricao = models.TextField() 

  def __str__(self) -> str:
    return self.genero
  
# Create your models here.
class Animais(models.Model):
  vacinacao_choices = [
    ("Sim", "Sim"),
    ("Não", "Não")
  ]
  nome = models.CharField(max_length=100)
  especie = models.ForeignKey(Especies, on_delete=models.DO_NOTHING)
  idade = models.IntegerField(validators=[MinValueValidator(0)], default=1)
  porte = models.ForeignKey(Porte, on_delete=models.DO_NOTHING)
  peso = models.IntegerField(validators=[MinValueValidator(0)], default=1)
  raça = models.ForeignKey(Raca, on_delete=models.DO_NOTHING)
  vacinacao_em_dia = models.CharField(max_length=3, choices=vacinacao_choices, default="Sim")
  cirurgias = models.CharField(max_length=200, default='Nenhuma')
  problemas_de_saude = models.CharField(max_length=200, default='Nenhum')
  medicacoes_atuais = models.CharField(max_length=200, default='Nenhuma')
  genero = models.ForeignKey(Genero, on_delete=models.DO_NOTHING)
  comportamento = models.CharField(max_length=255, default='Comportamento padrão') 
  photo = models.ImageField(upload_to='MEDIA_URL', blank=True, null=True)

  def __str__(self) -> str:
    return self.nome
  
  class Meta: 
    verbose_name = "Animal"
    verbose_name_plural = "Registro de animais"
    ordering = ["nome"]