from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart
from inventario.models import Producto
from .utils import get_or_create_cart

@login_required
def add_to_cart(request, product_id):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Producto, pk=product_id)
    cart.products.add(product)
    # Recalcular subtotal y total si es necesario
    cart.save()
    return redirect('carts:cart')

@login_required
def update_cart(request, product_id):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Producto, pk=product_id)
    new_quantity = request.POST.get('quantity')
    cart.products.update_or_create(product=product, defaults={'quantity': new_quantity})
    # Recalcular subtotal y total si es necesario
    cart.save()
    return redirect('carts:cart')

@login_required
def remove_from_cart(request, product_id):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Producto, pk=product_id)
    cart.products.remove(product)
    # Recalcular subtotal y total si es necesario
    cart.save()
    return redirect('carts:cart')

@login_required
def cart(request):
    cart = get_or_create_cart(request)
    return render(request, 'carts/cart.html', {'cart': cart})
