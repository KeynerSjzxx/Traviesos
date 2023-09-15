from django.contrib import admin
from django.urls import path
from landing import views
from facturacion import facturacion_views
from gestion_citas import citas_views
from PQRS import pqrs_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin:index'),
     path('carrito/', views.cart_view, name='carrito_view'),  # Asegúrate de que el
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('prod_carro/', facturacion_views.cart_view, name='carrito'),
    path('citas', citas_views.formulario_agendar, name='citas'),
    path('pqrs', pqrs_views.pqrs, name='pqrs'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('perfil', views.perfil, name='perfil'),
    path('datos', views.registro_informacion_adicional, name='datos'),
    path('registro/', views.registro, name='registro'),
    path('perfil', views.perfil, name='perfil'),
    path('comentarios', pqrs_views.coment, name='coment'),
]