from django.shortcuts import render, redirect
from .models import Producto, Fabrica 

from .forms import ProductoFormAdd
from django.contrib import messages
from django.utils import timezone
from django.db import connection


# Create your views here.
   
           
def listado_productos_view(request):
    contexto = {}
    productos = Producto.objects.all()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1 
    
    contexto["productos"] = productos
    contexto["num_visits"] = num_visits
    
    return render(request, "inventario/listado_productos.html", contexto)
    
def add_producto(request):
    contexto = {}
        
    if request.method == 'GET':
        contexto["form"] = ProductoFormAdd()
        return render(request, 'inventario/add_producto.html', contexto)
    
    if request.method == 'POST':   #
        
        form = ProductoFormAdd(request.POST)
        contexto["form"] = form 
        
        print(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, "Producto creado correctamente.")
            return redirect('listado_productos')
            
        else:
            messages.error(request, "Algo ha fallado, revise bien los datos ingresados.")
            return render(request, 'inventario/add_producto.html', contexto)
  
  
  
def detalle_producto(request, producto_id):
    contexto = {}
    try:
         
        producto =  Producto.objects.get(id = producto_id)
    except producto.DoesNotExist:
        messages.error(request, f"No existe el producto con id: {producto_id}")
        return redirect('index')
     
    contexto["producto"] = producto
     
     
    return render(request, 'inventario/detalle_producto.html', contexto)
 