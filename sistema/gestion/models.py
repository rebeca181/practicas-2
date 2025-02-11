from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from .choise import PUESTOS
from .valiladores import validar_cedula, validar_nombre, validar_salario, validar_positivo


class Empleados(models.Model):
    cedula = models.CharField(
        max_length=10,
        primary_key=True,
        validators=[
            MinLengthValidator(10),
            MaxLengthValidator(10),
            RegexValidator(r'^\d{10}$', 'La cédula debe contener exactamente 10 dígitos numéricos'),
            validar_cedula
        ]
    )
    nombre = models.CharField(max_length=100, validators=[validar_nombre])
    apellido = models.CharField(max_length=100, validators=[validar_nombre])
    puesto = models.CharField(max_length=100, choices=PUESTOS)
    salario = models.DecimalField(max_digits=10, decimal_places=2, validators=[validar_positivo])
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(10),
            MaxLengthValidator(10),
            RegexValidator(r'^\d{10}$', 'El teléfono debe contener exactamente 10 dígitos numéricos')
        ]
    )
    email = models.EmailField()

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'Empleados'

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.cedula})"


class Tipos_Pagos(models.Model):
    id_tipo_pago = models.AutoField(primary_key=True)
    nombre_tipo_pago = models.CharField(max_length=100, validators=[validar_nombre])
    descripcion = models.CharField(max_length=255)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Tipo de Pago'
        verbose_name_plural = 'Tipos de Pago'
        db_table = 'Tipos_Pagos'

    def __str__(self):
        return self.nombre_tipo_pago


class Servicios_Pagos(models.Model):
    id_salario = models.AutoField(primary_key=True, validators=[validar_positivo])
    id_tipo_pago = models.ForeignKey(Tipos_Pagos, on_delete=models.CASCADE)
    nombre_servicio_pago = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Servicio de Pago'
        verbose_name_plural = 'Servicios de Pago'
        db_table = 'Servicios_Pagos'

    def __str__(self):
        return self.nombre_servicio_pago
