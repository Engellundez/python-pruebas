from django.contrib import admin
from .models import *

# Register your models here.

# registramos el curso como parte del sitio de administración
# admin.site.register(Curso)


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    # datos a mostrar, de la bd
    # list_display = ('id', 'nombre', 'creditos')
    # datos a mostrar con metodos propios
    # list_display = ('id', 'datos', 'creditos')
    # datos a mostrar con meetodos de Curso
    list_display = ('id', 'coloreado', 'docente', 'creditos')
    # ordenar creditos desc y nombre asc
    # ordering = ('-creditos','nombre')
    # searching
    # search_fields = ('nombre',)
    # campos editables (No puede ser el campo linkeeable (default 0 de list_display))
    # list_editable = ('creditos',)
    # podemos utilizar el link para definir que campo va a ser nuestro link para editar.
    # list_display_links = ('nombre',)
    # genera un campo de filtros sobre los campos
    # list_filter = ('creditos',)
    # listar por pagina
    # list_per_page = 10
    # excluir de la edición
    # exclude = ('creditos',)

    # Creamos una estructura de opciones avanzadas dentro de la vista de cada 'Curso'
    # fieldsets = (
    #     (
    #         None,
    #         {
    #             'fields': ('nombre',)
    #         }
    #     ),
    #     (
    #         'Opciones Avanzadas',
    #         {
    #             'classes': ('collapse',),
    #             'fields': ('creditos',)
    #         }
    #     )
    # )

    # Generamos una modificación del objeto y pasamos a mayúsculas
    def datos(self, obj):
        return obj.nombre.upper()

    # definimos el titulo de nuestra modificación en la tabla (Solo aplica para modificaciones)
    datos.short_description = "CURSO (MAYÚSCULA)"
    datos.empty_value_display = '?? ??'
    datos.admin_order_field = 'nombre'

admin.site.register(Docente)
