from .models import Cart

def get_or_create_cart(request):
    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id')
    cart_instance, created = Cart.objects.get_or_create(cart_id=cart_id, defaults={'user': user})

    if created:
        request.session['cart_id'] = cart_instance.cart_id

    return cart_instance