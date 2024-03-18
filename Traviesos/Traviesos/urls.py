from django.contrib import admin
from django.urls import path, include
from landing import views
from gestion_citas import citas_views
from PQRS import pqrs_views

app_name = 'carts'

urlpatterns = [     
    path('admin/', admin.site.urls, name='admin:index'),
    path('carrito/', include('carts.urls')),
    path('juguetes/', views.juguetes, name='juguetes'),
    path('camas_muebles/', views.camas_muebles, name='camas_muebles'),
    path('ropas_accesorios/', views.ropas_accesorios, name='ropas_accesorios'),
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('Agendar', citas_views.formulario_agendar, name='citas'),
    path('perfil/citas/mascotas/datos_mascotas', citas_views.datos_mascota, name='datos_mascotas'),
    path('perfil/citas/mascotas/', citas_views.agregar_mascota, name='agregar_mascotas'),
    path('perfil/citas/mascotas/citas/lista_citas', citas_views.ver_citas, name='ver_citas'),
    path('eliminar_mascota/<int:mascota_id>/',citas_views.eliminar_mascota, name='eliminar_mascota'),
    path('editar_mascota/<int:mascota_id>/',citas_views.editar_mascota, name='editar_mascota'),
    path('eliminar_cita/<int:agendarCita_id>/',citas_views.eliminar_cita, name='eliminar_cita'),
    path('editar_cita/<int:agendarCita_id>/',citas_views.editar_cita, name='editar_cita'),
    path('pqrs/', pqrs_views.pqrs, name='pqrs'),
    path('tus_pqrs/pqrs', pqrs_views.pqrs, name='pqrs'),
    path('editar_pqrs/<int:PQRS_id>/',pqrs_views.editar_pqrs, name='editar_pqrs'),
    path('anular_pqrs/<int:pk>/', pqrs_views.anular_pqrs, name='anular_pqrs'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('datos/', views.registro_informacion_adicional, name='datos'),
    path('tus_pqrs/', pqrs_views.perfil_pqrs, name='perfil_pqrs'),
    path('procesar_compra/<int:producto_id>/', views.procesar_compra, name='procesar_compra'),
    path('confirmacion_Compra/', views.pagina_de_confirmacion, name='pagina_de_confirmacion'), 
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('compras', views.compra_perfil, name='compra_perfil')
]
