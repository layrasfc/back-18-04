from django.urls import path
from . import views

urlpatterns = [
  # Parte API
    path('clientes', views.listar_clientes),
    path('usuarios', views.ClientesView.as_view()),
    path('usuario/<int:pk>', views.ClientesDetailView.as_view())
]
