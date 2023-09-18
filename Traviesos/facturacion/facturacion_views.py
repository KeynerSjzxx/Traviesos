from django.shortcuts import render
from inventario.models import Producto
from carts.utils import get_or_create_cart
from .models import Cart  # Cambia "cart" a "Cart" para que coincida con el nombre de tu modelo

def cart_view(request):  # Cambia el nombre de la vista a "cart_view" para evitar conflictos con el nombre del modelo
    user = request.user if request.user.is_authenticated else None
    product_id = request.session.get('product_id')
    cart_instance = Cart.objects.filter(product_id=product_id).first()  # Cambia "cart" a "Cart"

    if cart_instance is None:
        cart_instance = Cart.objects.create(user=user)
        request.session['product_id'] = cart_instance.product_id

    return render(request, 'carrito/carrito.html', {
        'cart': cart_instance  # Pasa el carrito a la plantilla
    })

def add_to_cart(request):
    cart = get_or_create_cart(request)
    product_id = request.POST.get('product_id')  # Cambia "Productos" a "product_id" para obtener el ID del producto

    try:
        producto = Producto.objects.get(pk=product_id)
        cart.products.add(producto)
        return render(request, 'prod_carro/add.html', {
            'producto': producto  # Cambia "Productos" a "producto"
        })
    except Producto.DoesNotExist:
        # Manejar el caso en el que el producto no existe
        return render(request, 'prod_carro/producto_no_encontrado.html')  # Puedes crear una plantilla para esto