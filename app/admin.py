from django.contrib import admin
from .models import Cadastro, Contato
# Register your models here.

class CadastroAdmin(admin.ModelAdmin):
    list_display = ['data', 'responsavel', 'descricao', 'tipo', 'valor']
    list_editable = ['valor']
    search_fields = ['descricao']
    list_filter = ['responsavel', 'tipo']
    list_per_page = 5

admin.site.register(Cadastro, CadastroAdmin)
admin.site.register(Contato)