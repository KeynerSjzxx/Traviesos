from django.shortcuts import render

from inventario.models import Productos
from .utils import get_or_create_cart
from . models import cart

def cart(request):
    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id')
    cart = cart.objects.filter(cart_id=cart_id).first()

    if cart is None:
        cart = cart.objects.create(user=user)

        request.session['cart_id'] = cart.cart_id

        return render(request, 'carrito/carrito.html', {

        })
    
    def add(request):
        cart = get_or_create_cart(request)
        Productos = Productos.objects.get(pk=request.POST.get('product_id'))

        cart.productos.add(Productos)
        return render(request, 'prod_carro/add.html', {
            'Productos': Productos
        })