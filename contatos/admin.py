from django.contrib import admin

from contatos import models

from .models import Categoria, Contato

# Register your models here.


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    """Admin View for Contato"""

    list_display_links = (
        "id",
        "nome",
    )
    list_display = (
        "id",
        "nome",
        "sobrenome",
        "telefone",
        "categoria",
        "mostrar",
    )
    # list_filter = ("categoria",)
    list_editable = ("telefone", "mostrar")
    search_fields = ("telefone", "id", "nome", "sobrenome")
    ordering = ("-data_criacao",)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass
