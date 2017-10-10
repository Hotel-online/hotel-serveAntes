# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 13:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaHabitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'CategoriaHabitacion',
                'verbose_name_plural': 'CategoriaHabitaciones',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruc', models.CharField(max_length=11)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Person')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='DetalleReservacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('habitacionesR', models.IntegerField()),
                ('precio', models.FloatField(default=0)),
            ],
            options={
                'verbose_name': 'DetalleReservacion',
                'verbose_name_plural': 'DetalleReservaciones',
            },
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'DetalleVenta',
                'verbose_name_plural': 'DetalleVentas',
            },
        ),
        migrations.CreateModel(
            name='Doc_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bol', models.BooleanField(default=True)),
                ('fac', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Doc_Type',
                'verbose_name_plural': 'Doc_Types',
            },
        ),
        migrations.CreateModel(
            name='Forma_de_pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formaPago', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Forma_de_pago',
                'verbose_name_plural': 'Forma_de_pagos',
            },
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=60, null=True)),
                ('codigo', models.CharField(max_length=10)),
                ('detalle', models.TextField(blank=True, null=True)),
                ('precio_alquiler', models.FloatField(default=0.0)),
                ('estado', models.CharField(max_length=1)),
                ('categoriaHabitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.CategoriaHabitacion')),
            ],
            options={
                'verbose_name': 'Habitacion',
                'verbose_name_plural': 'Habitaciones',
            },
        ),
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_doc', models.CharField(max_length=15)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('total', models.FloatField(default=0)),
                ('forma_de_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Forma_de_pago')),
            ],
            options={
                'verbose_name': 'Reservacion',
                'verbose_name_plural': 'Reservaciones',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_doc', models.CharField(max_length=15)),
                ('numeroReservacion', models.IntegerField()),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.Cliente')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='doc_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Doc_Type'),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Venta'),
        ),
        migrations.AddField(
            model_name='detallereservacion',
            name='habitacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Habitacion'),
        ),
        migrations.AddField(
            model_name='detallereservacion',
            name='reservacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Reservacion'),
        ),
    ]
