from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Tipo_pqrs
from .forms import FormAgendarPqrs
from django.contrib.auth.decorators import login_required  # Importación añadida

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

def coment(request):
    return render(request, 'PQRS/coment.html')
