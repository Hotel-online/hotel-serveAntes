from django.db import models
from core.models import User, Person

# Create your models here.


class CategoriaHabitacion(models.Model):

    nombre = models.CharField(max_length=60)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "CategoriaHabitacion"
        verbose_name_plural = "CategoriaHabitaciones"

    def __str__(self):
        return '%s' % (self.nombre)


class Habitacion(models.Model):

    nombre = models.CharField(max_length=60, null=True, blank=True)
    codigo = models.CharField(max_length=10)
    detalle = models.TextField(null=True, blank=True)
    precio_alquiler = models.FloatField(default=0.0)
    estado = models.CharField(max_length=1)
    categoriaHabitacion = models.ForeignKey(CategoriaHabitacion)

    class Meta:
        verbose_name = "Habitacion"
        verbose_name_plural = "Habitaciones"

    def __str__(self):
        return '%s' % (self.nombre)


class Forma_de_pago(models.Model):

    formaPago = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Forma_de_pago"
        verbose_name_plural = "Forma_de_pagos"

    def __str__(self):
        return '%s' % (self.formaPago)


class Cliente(models.Model):

    ruc = models.CharField(max_length=11)
    person = models.OneToOneField(Person)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return '%s' % (self.ruc)


class Reservacion(models.Model):

    nro_doc = models.CharField(max_length=15)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.FloatField(default=0)
    forma_de_pago = models.ForeignKey(Forma_de_pago)

    class Meta:
        verbose_name = "Reservacion"
        verbose_name_plural = "Reservaciones"

    def __str__(self):
        return '%s' % (self.nro_doc)


class DetalleReservacion(models.Model):

    fecha = models.DateTimeField(auto_now_add=True)
    habitacionesR = models.IntegerField()
    precio = models.FloatField(default=0)
    habitacion = models.ForeignKey(Habitacion)
    reservacion = models.ForeignKey(Reservacion)

    class Meta:
        verbose_name = "DetalleReservacion"
        verbose_name_plural = "DetalleReservaciones"

    def __str__(self):
        return '%s ' % (self.habitacionesR)


class Venta(models.Model):

    nro_doc = models.CharField(max_length=15)
    numeroReservacion = models.IntegerField()
    vendedor = models.ForeignKey(User)
    cliente = models.ForeignKey(Cliente, blank=True, null=True)

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def __str__(self):
        return '%s' % (self.nro_doc)


class Doc_Type(models.Model):

    tipo_documento = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Doc_Type"
        verbose_name_plural = "Doc_Types"

    def __str__(self):
        return '%s' % (self.tipo_documento)


class DetalleVenta(models.Model):

    detalle = models.TextField(null=True, blank=True)
    venta = models.ForeignKey(Venta)
    doc_type = models.ForeignKey(Doc_Type)

    class Meta:
        verbose_name = "DetalleVenta"
        verbose_name_plural = "DetalleVentas"

    def __str__(self):
        return '%s' % (self.detalle)


class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='cars')
