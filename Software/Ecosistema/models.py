from django.db import models

# Create your models here.

class Ecosistema(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Ecosistema")
    tipo = models.CharField(max_length=50, verbose_name="Tipo de Ecosistema")
    area = models.FloatField(verbose_name="Área en km²")
    ubicacion = models.TextField(blank=True, null=True, verbose_name="Ubicación")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.tipo)
