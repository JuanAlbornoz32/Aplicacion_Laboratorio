from django.urls import path
from . import views

urlpatterns = [
    path("", views.insertar_view, name='index'),
    path("laboratorios/", views.mostrar_view, name='laboratorios'),
    path("editar/<int:pk>/", views.editar_view, name='editar'),
    path("eliminar/<int:pk>/", views.eliminar_view, name='eliminar'),
    
]
