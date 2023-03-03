from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    sueldo = models.FloatField()
    
    def __str__(self):
        return """Nombre: %s - 
        		Apellido: %s \n
                Edad: %d\n
                Sueldo: %.2f\n
                """ % (self.nombre,
                self.apellido,
                self.edad,
                self.sueldo)
