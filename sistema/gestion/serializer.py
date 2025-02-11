from rest_framework import serializers
from .models import Empleados, Tipos_Pagos, Servicios_Pagos

class EmpleadosSerializer(serializers.ModelSerializer):
    """ Serializador para el modelo Empleados """

    class Meta:
        model = Empleados
        fields = '__all__'  # Corregido

class TiposPagosSerializer(serializers.ModelSerializer):
    """ Serializador para el modelo Tipos_Pagos """

    class Meta:
        model = Tipos_Pagos
        fields = '__all__'  # Corregido

class ServiciosPagosSerializer(serializers.ModelSerializer):
    """ Serializador para el modelo Servicios_Pagos """

    class Meta:
        model = Servicios_Pagos
        fields = '__all__'  # Corregido
