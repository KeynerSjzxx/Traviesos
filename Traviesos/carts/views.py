from django.shortcuts import render

# Create your models here.
from inventario.models import Producto
from .models import Cart
from .utils import get_or_create_cart

def cart(request):
    Cart = get_or_create_cart(request)

    return render(request, 'productos/add.html', {

    })

def add(request):
    cart = get_or_create_cart(request)
    producto = producto.objects.get(pk=request.POST.get('product_id'))
    
    cart.products.add(producto)
    
    return render(request, 'prod_carro/add.html', {
        'product': producto
    })

