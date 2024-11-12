from django.db import models

# Create your models here.
class Empleados(models.Model):
    id_empleado=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    sexo=models.CharField(max_length=50)
    direccion=models.CharField(max_length=300)
    num_tel=models.CharField(max_length=10)
    email=models.CharField(max_length=200)
    nomina=models.CharField(max_length=300)

def __str__(self):
    return self.nombre