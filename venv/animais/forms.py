from dataclasses import fields
from pyexpat import model
from django import forms
from animais.models import Especies, Raca, Porte, Genero, Animais

class AnimaisForm(forms.ModelForm):
  class Meta:
    model = Animais
    fields = ['nome', 'especie', 'idade', 'porte', 'peso', 'raça',  'genero','vacinacao_em_dia', 'cirurgias', 'problemas_de_saude', 'medicacoes_atuais', 'comportamento', 'photo']

class EspeciesForm(forms.ModelForm):
  class Meta:
    model = Especies
    fields = ['especie', 'nome_cientifico', 'descricao']

class RacasForm(forms.ModelForm):
  class Meta:
    model = Raca
    fields = ['raca', 'descricao', 'especie']

class PortesForm(forms.ModelForm):
  class Meta:
    model = Porte
    fields = ['tipo', 'descrição']

class GenerosForm(forms.ModelForm):
  class Meta:
    model= Genero
    fields = ['genero', 'descricao']