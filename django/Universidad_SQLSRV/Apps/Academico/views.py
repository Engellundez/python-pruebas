# from django.http import HttpResponse
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from .models import Curso

# Create your views here.


def home(request):
    # Get all data from db Curso

    # obtener todo
    # cursos_list = Curso.objects.all()
    # obtener los primeros 5 registros
    # cursos_list = Curso.objects.all()[:5]
    # obtener los cursos del 4to al 9no registro
    # cursos_list = Curso.objects.all()[4:9]
    # orderBy ASC
    # cursos_list = Curso.objects.all().order_by('nombre')
    # orderBy DESC ocupa el - antes de la columna
    # cursos_list = Curso.objects.all().order_by('-nombre')
    # orderBy multivalue
    # cursos_list = Curso.objects.all().order_by('nombre', 'creditos')
    # cursos_list = Curso.objects.all().filter(nombre='Física',creditos=7)
    # LIKE '<data>%'
    # cursos_list = Curso.objects.all().filter(nombre__startswith='Q')
    # LIKE '%<data>%'
    # cursos_list = Curso.objects.all().filter(nombre__contains='g')
    # LIKE '%<data>'
    # cursos_list = Curso.objects.all().filter(nombre__endswith='n')

    cursos_list = Curso.objects.all()

    data = {
        'title': 'Gestión de Cursos',
        'cursos': cursos_list
    }

    return render(request, "gestionCursos.html", data)


class CursoListView(ListView):
    model = Curso
    template_name = 'gestionCursos.html'
    
    # podemos definir los datos a retornar
    def get_queryset(self) -> QuerySet[Any]:
        # retornamos todos los creditos <= a 4
        return Curso.objects.filter(creditos__lte=4)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Gestión de Cursos'})
        return context


