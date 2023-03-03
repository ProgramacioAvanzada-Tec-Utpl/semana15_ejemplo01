from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

# importar las clases de models.py
from manejo_empleados.models import *

# Create your views here.

def listar_empleados(request):
    """
        Listar los registros del modelo Empleado,
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # empleados
    empleados = Empleado.objects.all()
    # se obtiene el número de elementos de la lista
    numero_empleados = len(empleados)
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'empleados': empleados, 
    'numero_empleados': numero_empleados}
    return render(request, 'listar_empleados.html', informacion_template)
