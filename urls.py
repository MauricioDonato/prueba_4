from django.urls import path

from . import views
app_name = 'pasteleria'
urlpatterns = [
    path('', views.index, name='index'),
    path('frm_registrar_cli', views.frm_registrar_cli, name='frm_registrar_cli'),
    path('registrar_cliente', views.registrar_cliente, name='registrar_cliente'),
    path('cliente_regitrado', views.cliente_regitrado, name='cliente_regitrado' ),
    path('frm_buscar_cliente', views.frm_buscar_cliente, name='frm_buscar_cliente'),
    path('buscar_y_mostrar_cliente', views.buscar_y_mostrar_cliente, name='buscar_y_mostrar_cliente'),
    path('eliminar_cliente', views.eliminar_cliente, name='eliminar_cliente'),
    path('eliminador_cliente', views.eliminador_cliente, name='eliminador_cliente'),
    path('editar_cliente', views.editar_cliente, name='editar_cliente'),
    path('editador_cliente', views.editador_cliente, name='editador_cliente'),
    path('frm_comuna', views.frm_comuna, name='frm_comuna'),
    path('registrar_comuna', views.registrar_comuna, name='registrar_comuna'),
    path('frm_buscar_comuna', views.frm_buscar_comuna, name='frm_buscar_comuna'),
    path('buscar_y_mostrar_comuna', views.buscar_y_mostrar_comuna, name='buscar_y_mostrar_comuna'),
    path('eliminar_comuna', views.eliminar_comuna, name='eliminar_comuna'),
    path('eliminador_comuna', views.eliminador_comuna, name='eliminador_comuna'),
    path('editar_comuna', views.editar_comuna, name='editar_comuna'),
    path('editador_comuna', views.editador_comuna, name='editador_comuna'), 
    path('frm_producto', views.frm_producto, name='frm_producto'),
    path('registrar_producto', views.registrar_producto, name='registrar_producto'),
    path('frm_buscar_producto', views.frm_buscar_producto, name='frm_buscar_producto'),
    path('buscar_y_mostrar_producto', views.buscar_y_mostrar_producto, name='buscar_y_mostrar_producto'),
    path('eliminar_producto', views.eliminar_producto, name='eliminar_producto'), 
    path('eliminador_producto', views.eliminador_producto, name='eliminador_producto'),
    path('editar_producto', views.editar_producto, name='editar_producto'),
    path('editador_producto', views.editador_producto, name='editador_producto'),
]