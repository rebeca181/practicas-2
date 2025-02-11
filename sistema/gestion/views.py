from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Empleados, Tipos_Pagos, Servicios_Pagos
from gestion.serializer import EmpleadosSerializer, TiposPagosSerializer, ServiciosPagosSerializer

class EmpleadosViewSet(viewsets.ModelViewSet):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadosSerializer
    permission_classes = [IsAuthenticated]

class Tipos_PagosViewSet(viewsets.ModelViewSet):
    queryset = Tipos_Pagos.objects.all()
    serializer_class = TiposPagosSerializer
    permission_classes = [IsAuthenticated]

class Servicios_PagosViewSet(viewsets.ModelViewSet):
    queryset = Servicios_Pagos.objects.all()
    serializer_class = ServiciosPagosSerializer
    permission_classes = [IsAuthenticated]
