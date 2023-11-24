from django.contrib import admin
from .models import Colaboradores

# Register your models here.
@admin.register(Colaboradores)
class ColaboradoresAdmin(admin.ModelAdmin):
  list_display = ('nome_completo', 'endereço_de_email', 'cargo')
  list_filter = ('cargo',)
  search_fields = ('nome_completo', 'endereço_de_email')