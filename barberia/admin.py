from django.contrib import admin
from .models import (Clientes, Empleados, Servicios, Turnos, ServiciosTurnos, RegistrosDeAsistencias, Roles, Alquileres, Apertura, Descuentos, Liquidaciones, Categorias
)
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

@admin.register(RegistrosDeAsistencias)
class RegistrosDeAsistenciasAdmin(admin.ModelAdmin):
    list_display = ('id_asistencia', 'id_empleado', 'fecha', 'hora_entrada', 'hora_salida', 'estado')
    list_filter = ('estado', 'fecha')

@admin.register(Roles)
class RolesAdmin(admin.ModelAdmin):
    list_display = ('id_rol', 'nombre', 'descripcion')

@admin.register(Alquileres)
class AlquileresAdmin(admin.ModelAdmin):
    list_display = ('id_alquiler', 'id_empleado', 'fecha_inicio', 'fecha_fin', 'importe_acordado', 'estado')
    list_filter = ('estado',)

@admin.register(Apertura)
class AperturaAdmin(admin.ModelAdmin):
    list_display = ('id_apertura', 'id_empleado', 'fecha_hora', 'turno')

@admin.register(Descuentos)
class DescuentosAdmin(admin.ModelAdmin):
    list_display = ('id_descuento', 'nombre', 'mayorista', 'cantidad')
    list_filter = ('mayorista',)

@admin.register(Liquidaciones)
class LiquidacionesAdmin(admin.ModelAdmin):
    list_display = ('id_liquidacion', 'id_empleado', 'fecha_generacion', 'total_comision', 'total_a_pagar', 'estado')
    list_filter = ('estado',)

@admin.register(Categorias)
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'nombre', 'descripcion', 'estado')
    list_filter = ('estado',)
    search_fields = ('nombre',)
