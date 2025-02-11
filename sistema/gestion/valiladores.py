from rest_framework import serializers
from django.core.exceptions import ValidationError


def validar_cedula(value):
    """ Valida que la cédula tenga exactamente 10 dígitos numéricos """
    if not value.isdigit() or len(value) != 10:
        raise ValidationError("La cédula debe contener exactamente 10 dígitos numéricos.")
    return value

def validar_nombre(value):
    """ Valida que el nombre solo contenga letras """
    if not value.replace(" ", "").isalpha():
        raise ValidationError("El nombre solo puede contener letras y espacios.")
    return value


def validar_salario(value):
    """ Valida que el salario no sea menor a 100 """
    if value < 100:
        raise ValidationError("El salario debe ser mayor a 100.")
    return value

def validar_positivo(value):
    """ Valida que el valor sea positivo """
    if value <= 0:
        raise ValidationError("El valor debe ser positivo.")
    return value