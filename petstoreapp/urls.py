from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='index'),
    path('nosotros/', nosotros, name='nosotros'),
    path('galeria/', galeria, name='galeria'),
    path('formulario/', formulario, name='formulario'),
    path('api/', api, name='api'),
    path('lista_productos', lista_productos, name='lista_productos'),
    path('crear/', crear_producto, name='crear_producto'),
    path('modificar/<id>', modificar_producto, name='modificar_producto'),
    path('eliminar<id>', eliminar_producto, name='eliminar_producto'),
    path('registro/', registro_usuario, name='registro')
]