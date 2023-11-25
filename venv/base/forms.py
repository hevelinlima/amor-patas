from dataclasses import fields
from django import forms
from .models import SolicitacaoAdocao, ContactUs

class SolicitacaoAdocaoForm(forms.ModelForm):
    class Meta:
        model = SolicitacaoAdocao
        fields = ['nome_completo', 'animal_a_adotar', 'endereço_residencial', 'endereço_email', 'numero_de_telefone', 'tipo_de_residencia', 'tipo_de_propriedade', 'permissao_para_animais_no_local', 'motivacao_para_adotar', 'o_que_espera_da_adocao']

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['nome', 'endereço_de_email', 'mensagem']
