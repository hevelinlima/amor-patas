from django.contrib import admin
from animais.models import Animais

# Register your models here.
@admin.register(Animais)
class AnimaisAdmin(admin.ModelAdmin):
  list_display = ['nome', 'especie', 'idade', 'raça']
  search_fields = ['nome', 'especie']
  list_filter = ["especie"]