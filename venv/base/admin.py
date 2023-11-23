from django.contrib import admin
from base.models import SolicitacaoAdocao

@admin.register(SolicitacaoAdocao)
class SolicitacaoAdocaoAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'endereço_email', 'status')
    list_filter = ('status',)
    search_fields = ('nome_completo', 'endereço_email')
