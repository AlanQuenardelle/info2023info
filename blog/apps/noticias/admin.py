from django.contrib import admin

from .models import Categoria, Noticia, Contacto, Comentario
# Register your models here.

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria_noticia" , "fecha")
    ordering = ("-fecha",)

admin.site.register(Categoria)
admin.site.register(Noticia)
admin.site.register(Contacto)
admin.site.register(Comentario)
