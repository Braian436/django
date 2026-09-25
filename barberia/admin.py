from django.contrib import admin
from .models import (Clientes, Empleados, Servicios, Turnos, ServiciosTurnos, RegistrosDeAsistencias, Roles, Alquileres, Apertura, Descuentos, Liquidaciones, Categorias, Cajas, PagosAlquileres, Stock, Productos, Marcas, Compras, Ordenes, PagosOrden, MovimientosCaja, DetalleServicios, DetalleProductos, DetallesCompras
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

@admin.register(Cajas)
class CajasAdmin(admin.ModelAdmin):
    list_display = ('id_caja', 'id_apertura', 'saldo_incial', 'saldo_esperado', 'saldo_real', 'estado')

@admin.register(PagosAlquileres)
class PagosAlquileresAdmin(admin.ModelAdmin):
    list_display = ('id_pago_alquiler', 'id_alquiler', 'fecha', 'importe', 'estado', 'medio_pago')

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('id_stock', 'id_producto', 'cantidad_actual', 'stock_minimo', 'ultima_actualizacion')

@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre', 'id_marca', 'costo', 'estado')
    search_fields = ('nombre',)

@admin.register(Marcas)
class MarcasAdmin(admin.ModelAdmin):
    list_display = ('id_marca', 'nombre', 'id_categoria')

@admin.register(Compras)
class ComprasAdmin(admin.ModelAdmin):
    list_display = ('id_compra', 'nro_ticket', 'subtotal', 'total', 'fecha')

@admin.register(Ordenes)
class OrdenesAdmin(admin.ModelAdmin):
    list_display = ('id_orden', 'id_cliente', 'id_empleado', 'fecha_apertura', 'total_final')

@admin.register(PagosOrden)
class PagosOrdenAdmin(admin.ModelAdmin):
    list_display = ('id_pago_orden', 'id_orden', 'fecha', 'importe', 'estado', 'medio_pago')

@admin.register(MovimientosCaja)
class MovimientosCajaAdmin(admin.ModelAdmin):
    list_display = ('id_movimiento_caja', 'id_caja', 'tipo_movimiento', 'importe', 'fecha')
    list_filter = ('tipo_movimiento',)

@admin.register(DetalleServicios)
class DetalleServiciosAdmin(admin.ModelAdmin):
    list_display = ('id_detalle_servicio', 'id_orden', 'id_servicio', 'precio_actual', 'sub_total')

@admin.register(DetalleProductos)
class DetalleProductosAdmin(admin.ModelAdmin):
    list_display = ('id_detalle_producto', 'id_orden', 'id_producto', 'cantidad', 'sub_total')

@admin.register(DetallesCompras)
class DetallesComprasAdmin(admin.ModelAdmin):
    list_display = ('id_detalle_compra', 'id_compra', 'id_producto', 'cantidad', 'costo_unitario', 'sub_total')
