from django.contrib import admin

from .models import Empleados, Tipos_Pagos, Servicios_Pagos

admin.site.register(Empleados)
admin.site.register(Tipos_Pagos)
admin.site.register(Servicios_Pagos)
