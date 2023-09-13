from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from inventario.models import Producto
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
        cart = (request)
        Productos = Productos.objects.get(pk=request.POST.get('product_id'))

        cart.productos.add(Productos)
        return render(request, 'productos/add.html', {
            'Productos': Productos
        })
    
@login_required
def carrito_view(request):
    # Lógica de la vista
    return render(request, 'productos/add.html')  # Renderiza la plantilla 'carrito.html'
def juguetes (request):
    productos = Producto.objects.all()
    return render(request, 'productos/juguetes.html',{'productos':productos})
def camas (request):
    return render(request, 'productos/camas_muebles.html')
def ropa (request):
    return render(request, 'productos/ropas_accesorios.html')         