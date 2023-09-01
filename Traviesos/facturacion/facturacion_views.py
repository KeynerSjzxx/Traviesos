from django.shortcuts import render

def carrito_view(request):
    # Lógica de la vista
    return render(request, 'carrito/carrito.html')  # Renderiza la plantilla 'carrito.html'

def juguetes (request):
    return render(request, 'productos/juguetes.html')
def camas (request):
    return render(request, 'productos/camas_muebles.html')
def ropa (request):
    return render(request, 'productos/ropas_accesorios.html')         