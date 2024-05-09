from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  # Tem que colocar /api/ antes do caminho
    path('clientes', views.listar_clientes),
    path('usuarios', views.ClientesView.as_view()),
    path('usuario/<int:pk>', views.ClientesDetailView.as_view())
    

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # o endereço da imagem virá depois da url, passamos o endereço da pasta das imagens

