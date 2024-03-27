from django.db import models
from django.utils.html import format_html
from .choices import sexos

# Create your models here.


class Docente(models.Model):
    # verbose_name define el nombre de representación del campo
    apellido_paterno = models.CharField(
        max_length=20, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(
        max_length=20, verbose_name='Apellido Materno')
    nombres = models.CharField(max_length=20, verbose_name='Nombres')
    fecha_nacimiento = models.DateField(
        auto_now=False, verbose_name='Fecha de Nacimiento')
    sexo = models.CharField(max_length=1, choices=sexos, default='F')

    @property
    def nombre_completo(self):
        return f'{self.apellido_paterno} {self.apellido_materno}, {self.nombres}'

    def __str__(self):
        return self.nombre_completo

    # cargamos los metadatos y permite actualizarlos
    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
        db_table = 'docente'
        ordering = ['apellido_paterno', '-apellido_materno']


class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    # creando una relación
    docente = models.ForeignKey(Docente,null=True,blank=True,on_delete=models.CASCADE)

    # esto en django es equivalente a __repr__ que también da una representación del dato
    def __str__(self) -> str:
        texto = f'{self.nombre} ({self.creditos})'
        return texto

    def coloreado(self):
        if self.creditos >= 4:
            return format_html(f'<span style="color: blue">{self.nombre}</span>')
        else:
            return format_html(f'<span style="color: red">{self.nombre}</span>')
