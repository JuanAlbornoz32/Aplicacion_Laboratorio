from django.urls import path
from . import views

urlpatterns = [
    path("", views.insertar_view, name='insertar'),
    path("mostrar/", views.mostrar_view, name='mostrar'),
    path("editar/<int:pk>/", views.editar_view, name='editar'),
    path("editar/actualizarlaboratorio/<int:pk>/", views.actualizar_view, name='actualizar'),
    path("eliminar/<int:pk>/", views.eliminar_view, name='eliminar'),
    
]
