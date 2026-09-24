from django.contrib import admin
from .models import Clientes, Empleados, Servicios, Turnos, ServiciosTurnos

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('id_clientes', 'nombre', 'apellido', 'telefono', 'email', 'estado')
    search_fields = ('nombre', 'apellido', 'telefono', 'email')

@admin.register(Empleados)
class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ('id_empleado', 'nombre_empleado', 'dni', 'estado')
    search_fields = ('nombre_empleado', 'dni')

@admin.register(Servicios)
class ServiciosAdmin(admin.ModelAdmin):
    list_display = ('id_servicio', 'nombre', 'precio', 'estado')
    list_filter = ('estado',)

@admin.register(Turnos)
class TurnosAdmin(admin.ModelAdmin):
    list_display = ('id_turno', 'fecha', 'hora', 'id_clientes', 'id_empleado', 'estado')
    list_filter = ('estado', 'fecha')

@admin.register(ServiciosTurnos)
class ServiciosTurnosAdmin(admin.ModelAdmin):
    list_display = ('id_servicio_turno', 'id_servicio', 'orden')