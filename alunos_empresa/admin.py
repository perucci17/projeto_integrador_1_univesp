from django.contrib import admin
from alunos_empresa.models import Usuario

# Register your models here.

class UsuarioAdmin (admin.ModelAdmin):
    list_display = ('nome' , 'tipo_usuario', 'curso_solicitado')

admin.site.register(Usuario, UsuarioAdmin)
