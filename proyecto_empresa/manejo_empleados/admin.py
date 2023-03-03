from django.contrib import admin

# Importar las clases del modelo
from manejo_empleados.models import Empleado

# Agregar la clase Equipo para administrar desde
# interfaz de administración
admin.site.register(Empleado)
