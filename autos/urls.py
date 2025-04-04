from django.urls import path
from . import views

urlpatterns = [
    
    path('marcas/', views.lista_marcas, name='lista_marcas'),
    path('marcas/crear/', views.crear_marca, name='crear_marca'),
    path('marcas/editar/<int:pk>/', views.editar_marca, name='editar_marca'),
    path('marcas/eliminar/<int:pk>/', views.eliminar_marca, name='eliminar_marca'),

    
    path('', views.lista_autos, name='lista_autos'),
    path('crear/', views.crear_auto, name='crear_auto'),
    path('editar/<int:pk>/', views.editar_auto, name='editar_auto'),
    path('eliminar/<int:pk>/', views.eliminar_auto, name='eliminar_auto'),

    
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/crear/', views.crear_cliente, name='crear_cliente'),
    path('clientes/editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:pk>/', views.eliminar_cliente, name='eliminar_cliente'),

    
    path('inicio/', views.inicio, name='inicio'),
]

