from django.contrib import admin
from .models import *

# Register your models here.

# registramos el curso como parte del sitio de administración
# admin.site.register(Curso)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    # datos a mostrar, si no error
    list_display = ('id','nombre', 'creditos')
    # ordenar creditos desc y nombre asc
    ordering = ('-creditos','nombre')
    # searching
    # search_fields = ('nombre',)
    # campos editables (No puede ser el campo linkeeable (default 0 de list_display))
    # list_editable = ('creditos',)
    # podemos utilizar el link para definir que campo va a ser nuestro link para editar.
    # list_display_links = ('nombre',)
    # genera un campo de filtros sobre los campos
    # list_filter = ('creditos',)
    # listar por pagina
    list_per_page = 10
    # excluir de la edición
    # exclude = ('creditos',)


# admin.site.register(Curso,CursoAdmin)