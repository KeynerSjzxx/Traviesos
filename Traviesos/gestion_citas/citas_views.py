from django.shortcuts import render

def citas (request):
    return render(request,'citas/citas.html')
