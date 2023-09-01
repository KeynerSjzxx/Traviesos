from django.shortcuts import render

def carrito_view(request):
    # Lógica de la vista
    return render(request, 'carrito.html')  # Renderiza la plantilla 'carrito.html'
