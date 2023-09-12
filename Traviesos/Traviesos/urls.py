"""
URL configuration for Traviesos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from landing import views
from facturacion import facturacion_views
from gestion_citas import citas_views
from PQRS import pqrs_views

urlpatterns = [
    path('carrito/', views.carrito_compras, name='carrito_compras'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('quitar_del_carrito/<int:producto_id>/', views.quitar_del_carrito, name='quitar_del_carrito'),
    path('admin/', admin.site.urls, name='admin:index'),
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('carrito', facturacion_views.carrito_view, name='carrito'),
    path('juguetes', facturacion_views.juguetes, name='juguetes'),
    path('camas', facturacion_views.camas, name='camas_muebles'),
    path('ropa', facturacion_views.ropa, name='ropas_accesorios'),
    path('citas', citas_views.formulario_agendar, name='citas'),
    path('pqrs', pqrs_views.formulario_pqrs, name='pqrs'),
    path('logout/', views.logout_view, name='logout'),
<<<<<<< HEAD
    path('registro/', views.crear_cuenta, name='registro'),
    path('perfil', views.perfil, name='perfil'),
    path('form.html', pqrs_views.formulario_pqrs, name='pqrs_form')
=======
    path('registro/', views.registro, name='registro'),
    path('perfil', views.perfil, name='perfil'),
    path('datos', views.registro_informacion_adicional, name='datos'),
    
>>>>>>> 50df9a6111a0b8b0cc999e1bf99a9c4023221809
]
