from django.shortcuts import render
from django.contrib import messages
from .forms import FormAgendarCita
from django.contrib.auth.decorators import login_required

@login_required
def formulario_agendar(request):
    if request.method == 'POST':
        form = FormAgendarCita(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cita guardada correctamente.')
            form = FormAgendarCita()
        else:
            messages.error(request, 'Error al agendar la cita. Revise los datos.')
            # Agrega mensajes de error específicos para cada campo con errores
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error en el campo {field}: {error}')
    else:
        form = FormAgendarCita()

    context = {'form': form}
    return render(request, 'citas/citas.html', context)
