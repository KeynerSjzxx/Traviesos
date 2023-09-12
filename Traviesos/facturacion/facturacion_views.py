from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from inventario.models import Producto


@login_required
def carrito_view(request):
    # Lógica de la vista
    return render(request, 'carrito/carrito.html')  # Renderiza la plantilla 'carrito.html'
def juguetes (request):
    productos = Producto.objects.all()
    return render(request, 'productos/juguetes.html',{'productos':productos})
def camas (request):
    return render(request, 'productos/camas_muebles.html')
def ropa (request):
    return render(request, 'productos/ropas_accesorios.html')         