from django.shortcuts import render, redirect  # Añade "redirect" para redirigir a otra página

# Importa tus modelos y funciones necesarios
from inventario.models import Producto
from .models import Cart
from .utils import get_or_create_cart

def cart(request):
    # Utiliza un nombre de variable diferente para evitar conflicto con el modelo "Cart"
    cart_instance = get_or_create_cart(request)

    return render(request, 'productos/add.html', {
        'cart': cart_instance  # Pasa el carrito a la plantilla
    })

def add(request):
    cart = get_or_create_cart(request)
    product_id = request.POST.get('product_id')  # Cambia "producto" a "product_id" para obtener el ID del producto

    try:
        # Utiliza "Producto" en lugar de "producto" y "get" en lugar de "get_object_or_404" si prefieres manejar excepciones
        producto = Producto.objects.get(pk=product_id)
        cart.products.add(producto)
        return redirect('nombre_de_la_vista')  # Redirige a una vista apropiada después de agregar el producto
    except Producto.DoesNotExist:
        # Manejar el caso en el que el producto no existe
        return render(request, 'prod_carro/producto_no_encontrado.html')  # Puedes crear una plantilla para esto

