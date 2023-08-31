from django.shortcuts import render

def index (request):
    return render(request, 'index.html')

def premios (request):
    return render(request, 'productos/premios.html')    
def login_view (request):
    return render(request,'login/login.html')