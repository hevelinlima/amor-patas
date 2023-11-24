from django import forms
from .models import Colaboradores

class ColaboradoresForm(forms.ModelForm):
  class Meta:
    model = Colaboradores
    fields = ['nome_completo', 'endereço_residencial', 'endereço_de_email', 'numero_de_telefone', 'cargo', 'formaçao_ou_certificações', 'restriçoes_ou_condiçoes_de_saude', 'contato_de_emergencia', 'nome_do_contato_de_emergencia', 'foto']