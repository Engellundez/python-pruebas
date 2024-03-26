from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    
    # esto en django es equivalente a __repr__ que también da una representación del dato
    def __str__(self) -> str:
        texto = f'{self.nombre} ({self.creditos})'
        return texto