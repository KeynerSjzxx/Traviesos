from django.shortcuts import render
from django.http import HttpResponse

def carrito_view(request):
    context = {
        'mensaje': 'Hola desde la vista!',
    }
    return render(request, 'carrito/html', context)




