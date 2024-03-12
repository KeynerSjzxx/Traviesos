from django.shortcuts import render
from templates import productos
from .models import Cart
from . utils import get_or_create_cart

def cart(request):
    cart = get_or_create_cart(request)

        
    return render(request, 'carts/cart.html', {
        
    })

def add(request):   
    product = product.objects.get(pk=request.POST.get('product_id'))

    cart.products.add(product)

    return render(request, 'carts/add.thml', {
        'product': product
    })