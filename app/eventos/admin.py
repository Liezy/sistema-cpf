from django.contrib import admin

# Register your models here.
from .models import Servidor, Evento, Presenca

@admin.register(Servidor)
class ServidorAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome', 'setor', 'email')
    search_fields = ('cpf', 'nome', 'setor', 'email')

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data', 'local')
    search_fields = ('nome', 'data', 'local')

@admin.register(Presenca)
class PresencaAdmin(admin.ModelAdmin):
    list_display = ('servidor', 'evento', 'data_hora', 'sincronizado')
    search_fields = ('servidor__nome', 'evento__nome')
    list_filter = ('sincronizado', 'data_hora')