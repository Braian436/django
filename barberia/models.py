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
