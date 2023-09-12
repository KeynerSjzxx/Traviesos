from django.shortcuts import render

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