from django.contrib import admin
from animais.models import Animais, Especies, Porte, Raca, Genero

# Register your models here.
@admin.register(Animais)
class AnimaisAdmin(admin.ModelAdmin):
  list_display = ['nome', 'especie', 'idade', 'raça']
  search_fields = ['nome', 'especie']
  list_filter = ["especie"]

@admin.register(Especies)
class EspeciesAdmin(admin.ModelAdmin):
  list_display = ['especie']

@admin.register(Porte)
class PorteAdmin(admin.ModelAdmin):
  list_display = ['tipo']

@admin.register(Raca)
class RacaAdmin(admin.ModelAdmin):
  list_display = ['raca']

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
  list_display = ['genero']