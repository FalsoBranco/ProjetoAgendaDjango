from django.contrib import admin

from contatos import models

from .models import Categoria, Contato

# Register your models here.


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    pass
    
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

