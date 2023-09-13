from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def pqrs (request):
    return render(request,'PQRS/form.html', {'user': request.user})

def coment (request):
    return render(request, 'PQRS/coment.html')
