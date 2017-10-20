from django.contrib import admin
from hotel.models import Reservacion
from hotel.models import CategoriaHabitacion
from hotel.models import Habitacion
from hotel.models import DetalleReservacion
from hotel.models import Forma_de_pago
from hotel.models import Cliente
from hotel.models import Venta
from hotel.models import DetalleVenta
from hotel.models import Doc_Type
from hotel.models import Car


# Register your models here.
admin.site.register(Reservacion)
admin.site.register(CategoriaHabitacion)
admin.site.register(Habitacion)
admin.site.register(DetalleReservacion)
admin.site.register(Forma_de_pago)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(Doc_Type)
admin.site.register(Car)
