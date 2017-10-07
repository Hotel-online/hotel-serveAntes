from django.db import models

# Create your models here.


class CategoriaHabitacion(models.Model):

    nombre = models.CharField(max_length=60)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "CategoriaHabitacion"
        verbose_name_plural = "CategoriaHabitaciones"

    def __str__(self):
        return '%s' % (self.nombre)


class Reservacion(models.Model):

    nro_doc = models.CharField(max_length=15)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.FloatField(default=0)

    class Meta:
        verbose_name = "Reservacion"
        verbose_name_plural = "Reservaciones"

    def __str__(self):
        return '%s' % (self.nro_doc)
