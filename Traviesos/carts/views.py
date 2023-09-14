from django.shortcuts import render, redirect  # Añade "redirect" para redirigir a otra página

# Importa tus modelos y funciones necesarios
from inventario.models import Producto
from .models import Cart
from .utils import get_or_create_cart
from .models import Cart  # Importa el modelo Cart

def cart_view(request):
    user = request.user if request.user.is_authenticated else None
    cart_instance = Cart.objects.filter(users=user).first()  # Obtén el carrito del usuario

    if cart_instance is None:
        # Si el carrito no existe, puedes manejarlo como desees (crear uno, redirigir, etc.)
        # En este ejemplo, simplemente lo inicializaremos a una lista vacía de productos.
        cart_products = []
    else:
        # Obtén los productos en el carrito
        cart_products = cart_instance.products.all()

    return render(request, 'carrito/carrito.html', {
        'cart_products': cart_products  # Pasa los productos al contexto
    })

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

