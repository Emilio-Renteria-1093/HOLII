from django.db import models

# Create your models here.
class ventas(models.Model):
    id_venta =models.CharField(primary_key=True, max_length=6)
    id_cliente=models.CharField(max_length=8)
    id_empleado=models.CharField(max_length=12)


    def __str__(self):
        return self.id_cliente
