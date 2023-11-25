from django.contrib import admin
from base.models import SolicitacaoAdocao, ContactUs

@admin.register(SolicitacaoAdocao)
class SolicitacaoAdocaoAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'endereço_email', 'status')
    list_filter = ('status',)
    search_fields = ('nome_completo', 'endereço_email')
    
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereço_de_email')
    list_filter= ('nome',)
    search_fields = ('nome', 'endereço_de_email')
