from django.shortcuts import render

# Create your models here.
from inventario.models import Producto
from .models import Cart
from .utils import get_or_create_cart

def cart(request):

    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id') 

    if request.session.get('cart_id'):
        cart = Cart.objects.get(pk=request.session.get('cart_id'))
    else:
        cart = Cart.objects.create(user=user)

        request.session['cart_id'] = cart.id

    Cart = get_or_create_cart(request)

    return render(request, 'productos/add.html', {

    })

def add(request):
    cart = get_or_create_cart(request)
    producto = producto.objects.get(pk=request.POST.get('product_id'))

