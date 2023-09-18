from django.contrib import admin
from django.urls import path
from landing import views
from django.urls import include
from gestion_citas import citas_views
from PQRS import pqrs_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin:index'),
    path('carrito/', include('carts.urls')),
    path('juguetes/', views.juguetes, name='juguetes'),
    path('camas_muebles/', views.juguetes, name='camas_muebles'),
    path('ropas_accesorios/', views.juguetes, name='ropas_accesorios'),
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
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