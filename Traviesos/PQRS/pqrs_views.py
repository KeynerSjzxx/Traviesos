from django.shortcuts import render
from django.contrib import messages
from .models import Tipo_pqrs
from .forms import FormAgendarPqrs
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import PQRS

def formulario_pqrs(request):
    if request.method == 'POST':
        form = FormAgendarPqrs(request.POST)
        if form.is_valid():
            tipo_pqrs_id = request.POST.get('Tipo_pqrs')
            try:
                tipo_pqrs = Tipo_pqrs.objects.get(pk=tipo_pqrs_id)
                form.instance.Tipo_pqrs = tipo_pqrs
                form.save()
                messages.success(request, 'Mensaje enviado exitosamente.')
                form = FormAgendarPqrs()
            except Tipo_pqrs.DoesNotExist:
                messages.error(request, 'El tipo de PQRS seleccionado no existe.')
        else:
            messages.error(request, 'Error al enviar el mensaje. Revise los datos.')
            
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error en el campo {field}: {error}')
    else:
        form = FormAgendarPqrs()

    context = {'form': form}
    return render(request, 'PQRS/form.html', context)

def mostrar_formulario(request):
    return render(request, 'PQRS/form.html')

@login_required
def pqrs(request):
    return render(request, 'PQRS/form.html', {'user': request.user})

@login_required
def perfil_pqrs(request):
    usuario = User.objects.get(username=request.user.username)
    pqrs_usuario = PQRS.objects.filter(Nombre=usuario)
    return render(request, 'PQRS/PQRS_cliente.html', {'usuario': usuario, 'pqrs_usuario': pqrs_usuario})