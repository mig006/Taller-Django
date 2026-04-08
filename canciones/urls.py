from django.urls import path
from . import views

urlpatterns = [
    path('', views.cancion_lista, name='cancion_lista'),
    path('nueva/', views.cancion_crear, name='cancion_crear'),
    path('<int:pk>/', views.cancion_detalle, name='cancion_detalle'),
    path('<int:pk>/editar/', views.cancion_editar, name='cancion_editar'),
    path('<int:pk>/eliminar/', views.cancion_eliminar, name='cancion_eliminar'),
]
