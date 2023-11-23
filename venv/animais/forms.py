from django import forms
from animais.models import Especies, Raca, Porte, Genero, Animais

class AnimaisForm(forms.ModelForm):
  class Meta:
    model = Animais
    fields = ['nome', 'especie', 'idade', 'porte', 'peso', 'raça',  'genero','vacinacao_em_dia', 'cirurgias', 'problemas_de_saude', 'medicacoes_atuais', 'comportamento', 'photo']