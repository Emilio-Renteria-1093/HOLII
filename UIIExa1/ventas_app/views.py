from django.shortcuts import render
from .models import ventas

# Create your views here.
def inicio_vista(request):
    # obtener todos los registros de la tabla materia
    Listadoventas=ventas.objects.all()
    return render(request,"gestionarventas.html",{"lasventas":Listadoventas})