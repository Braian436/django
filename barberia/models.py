from django.db import models

class Clientes(models.Model):
    id_clientes = models.BigAutoField(primary_key=True)
    telefono = models.CharField(max_length=30)
    estado = models.BooleanField(blank=True, null=True, default=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=150, unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Clientes'

    def __str__(self):
        return f"{self.nombre or ''} {self.apellido or ''}".strip() or f"Cliente #{self.id_clientes}"


class Empleados(models.Model):
    id_empleado = models.IntegerField(primary_key=True)
    nombre_empleado = models.CharField(max_length=50, blank=True, null=True)
    foto_empleado = models.BinaryField(blank=True, null=True)
    dni = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=150, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    fecha_alta = models.DateTimeField(blank=True, null=True)
    ultimo_acceso = models.DateTimeField(blank=True, null=True)
    porcentaje_comision = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleados'

    def __str__(self):
        return self.nombre_empleado or f"Empleado #{self.id_empleado}"


class Servicios(models.Model):
    id_servicio = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    estado = models.BooleanField(blank=True, null=True, default=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    id_empleado = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='id_empleado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicios'

    def __str__(self):
        return f"{self.nombre or 'Servicio'} (${self.precio or 0})"


class Turnos(models.Model):
    id_turno = models.BigAutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField(blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True, default='pendiente')
    observacion = models.CharField(max_length=255, blank=True, null=True)
    id_clientes = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_clientes', blank=True, null=True)
    id_empleado = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='id_empleado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'turnos'

    def __str__(self):
        return f"Turno #{self.id_turno} - {self.fecha} {self.hora or ''}"


class ServiciosTurnos(models.Model):
    id_servicio_turno = models.IntegerField(primary_key=True)
    orden = models.IntegerField(blank=True, null=True)
    id_servicio = models.ForeignKey(Servicios, models.DO_NOTHING, db_column='id_servicio', blank=True, null=True)
    id_turno = models.ForeignKey(Turnos, models.DO_NOTHING, db_column='id_turno', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicios_turnos'

    def __str__(self):
        return f"ServicioTurno #{self.id_servicio_turno} (Orden {self.orden})"

class RegistrosDeAsistencias(models.Model):
    id_asistencia = models.AutoField(primary_key=True)
    id_empleado = models.ForeignKey('Empleados', models.DO_NOTHING, db_column='id_empleado', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    hora_entrada = models.TimeField(blank=True, null=True)
    hora_salida = models.TimeField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    observaciones = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registros_de_asistencias'

    def __str__(self):
        return f"RegistroDeAsistencia #{self.id_asistencia} - {self.fecha}"


class Roles(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=240, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'

    def __str__(self):
        return self.nombre or f"Rol #{self.id_rol}"

class Alquileres(models.Model):
    id_alquiler = models.AutoField(primary_key=True)
    id_empleado = models.ForeignKey('Empleados', models.DO_NOTHING, db_column='id_empleado', blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    importe_acordado = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alquileres'

    def __str__(self):
        return f"Alquiler #{self.id_alquiler} - {self.id_empleado} ({self.fecha_inicio})"


class Apertura(models.Model):
    id_apertura = models.AutoField(primary_key=True)
    id_empleado = models.ForeignKey('Empleados', models.DO_NOTHING, db_column='id_empleado', blank=True, null=True)
    fecha_hora = models.DateTimeField(blank=True, null=True)
    turno = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apertura'

    def __str__(self):
        return f"Apertura #{self.id_apertura} - {self.id_empleado} ({self.fecha_hora})"


class Descuentos(models.Model):
    id_descuento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    mayorista = models.BooleanField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'descuentos'

    def __str__(self):
        return self.nombre or f"Descuento #{self.id_descuento}"


class Liquidaciones(models.Model):
    id_liquidacion = models.AutoField(primary_key=True)
    id_empleado = models.ForeignKey('Empleados', models.DO_NOTHING, db_column='id_empleado', blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_generacion = models.DateField(blank=True, null=True)
    total_comision = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_a_pagar = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'liquidaciones'

    def __str__(self):
        return f"Liquidación #{self.id_liquidacion} - {self.id_empleado} ({self.fecha_generacion})"


class Categorias(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    descripcion = models.CharField(max_length=80, blank=True, null=True)
    estado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias'

    def __str__(self):
        return self.nombre or f"Categoría #{self.id_categoria}"

class Cajas(models.Model):
    id_caja = models.AutoField(primary_key=True)
    id_apertura = models.ForeignKey('Apertura', models.DO_NOTHING, db_column='id_apertura', blank=True, null=True)
    fecha_apertura = models.DateTimeField(blank=True, null=True)
    fecha_cierre = models.DateTimeField(blank=True, null=True)
    saldo_incial = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    saldo_esperado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    saldo_real = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    diferencia = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cajas'

    # Cajas
    def __str__(self):
        return f"Caja #{self.id_caja} - {self.fecha_apertura}"


class PagosAlquileres(models.Model):
    id_pago_alquiler = models.AutoField(primary_key=True)
    id_alquiler = models.ForeignKey('Alquileres', models.DO_NOTHING, db_column='id_alquiler', blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    importe = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estado = models.BooleanField(blank=True, null=True)
    medio_pago = models.CharField(max_length=30, blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pagos_alquileres'

    # PagosAlquileres
    def __str__(self):
        return f"Pago alquiler #{self.id_pago_alquiler} - {self.id_alquiler} (${self.importe})"


class Stock(models.Model):
    id_stock = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    cantidad_actual = models.IntegerField(blank=True, null=True)
    stock_minimo = models.IntegerField(blank=True, null=True)
    ultima_actualizacion = models.DateTimeField(blank=True, null=True)
    tipo_movimiento = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock'

    # Stock
    def __str__(self):
        return f"Stock {self.id_producto} - {self.cantidad_actual} u."


class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    id_marca = models.ForeignKey('Marcas', models.DO_NOTHING, db_column='id_marca', blank=True, null=True)
    id_descuento = models.ForeignKey('Descuentos', models.DO_NOTHING, db_column='id_descuento', blank=True, null=True)
    codigo_barra = models.BigIntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    estado = models.BooleanField(blank=True, null=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos'

    # Productos
    def __str__(self):
        return self.nombre or f"Producto #{self.id_producto}"


class Marcas(models.Model):
    id_marca = models.AutoField(primary_key=True)
    id_categoria = models.ForeignKey('Categorias', models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marcas'

    # Marcas
    def __str__(self):
        return self.nombre or f"Marca #{self.id_marca}"


class Compras(models.Model):
    id_compra = models.AutoField(primary_key=True)
    nro_ticket = models.IntegerField(unique=True, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compras'

    # Compras
    def __str__(self):
        return f"Compra #{self.id_compra} - Ticket {self.nro_ticket} (${self.total})"



class Ordenes(models.Model):
    id_orden = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey('Clientes', models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_empleado = models.ForeignKey('Empleados', models.DO_NOTHING, db_column='id_empleado', blank=True, null=True)
    fecha_apertura = models.DateTimeField(blank=True, null=True)
    fecha_cierre = models.DateTimeField(blank=True, null=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    descuentos = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    total_final = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    observaciones = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ordenes'

    def __str__(self):
        return f"Orden #{self.id_orden} - {self.id_cliente} (${self.total_final})"

class PagosOrden(models.Model):
    id_pago_orden = models.AutoField(primary_key=True)
    id_orden = models.ForeignKey(Ordenes, models.DO_NOTHING, db_column='id_orden', blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    importe = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estado = models.BooleanField(blank=True, null=True)
    medio_pago = models.CharField(max_length=30, blank=True, null=True)
    observaciones = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pagos_orden'

    # PagosOrden
    def __str__(self):
        return f"Pago orden #{self.id_pago_orden} - {self.id_orden} (${self.importe})"



class MovimientosCaja(models.Model):
    id_movimiento_caja = models.AutoField(primary_key=True)
    id_pago_alquiler = models.ForeignKey(PagosAlquileres, models.DO_NOTHING, db_column='id_pago_alquiler', blank=True, null=True)
    id_pago_orden = models.ForeignKey(PagosOrden, models.DO_NOTHING, db_column='id_pago_orden', blank=True, null=True)
    id_compra = models.ForeignKey(Compras, models.DO_NOTHING, db_column='id_compra', blank=True, null=True)
    id_caja = models.ForeignKey(Cajas, models.DO_NOTHING, db_column='id_caja', blank=True, null=True)
    importe = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    tipo_movimiento = models.CharField(max_length=150, blank=True, null=True)
    concepto = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movimientos_caja'

    # MovimientosCaja
    def __str__(self):
        return f"Movimiento #{self.id_movimiento_caja} - {self.tipo_movimiento} (${self.importe})"


class DetalleServicios(models.Model):
    id_detalle_servicio = models.AutoField(primary_key=True)
    id_orden = models.ForeignKey(Ordenes, models.DO_NOTHING, db_column='id_orden', blank=True, null=True)
    id_servicio = models.ForeignKey('Servicios', models.DO_NOTHING, db_column='id_servicio', blank=True, null=True)
    precio_actual = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_servicios'

    # DetalleServicios
    def __str__(self):
        return f"Detalle servicio #{self.id_detalle_servicio} - {self.id_servicio}"


class DetalleProductos(models.Model):
    id_detalle_producto = models.AutoField(primary_key=True)
    id_orden = models.ForeignKey(Ordenes, models.DO_NOTHING, db_column='id_orden', blank=True, null=True)
    id_producto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_productos'

    # DetalleProductos
    def __str__(self):
        return f"Detalle producto #{self.id_detalle_producto} - {self.id_producto} x{self.cantidad}"
