from django.contrib import admin
from django.urls import path
from landing import views
from facturacion import facturacion_views
from gestion_citas import citas_views
from PQRS import pqrs_views

urlpatterns = [
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
    path('registro/', views.crear_cuenta, name='registro'),
    path('perfil', views.perfil, name='perfil'),
    path('form.html', pqrs_views.formulario_pqrs, name='pqrs_form'),
    path('registro/', views.registro, name='registro'),
    path('perfil', views.perfil, name='perfil'),
    path('datos', views.registro_informacion_adicional, name='datos'),
]
