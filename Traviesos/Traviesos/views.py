from django.shortcuts import render

def index (request):
    return render(request, 'index.html')

def premios (request):
    return render(request, 'premios.html')    