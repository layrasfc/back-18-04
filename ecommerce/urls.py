
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

# Verificação de login
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from api import views # pegar as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

    # Responsáveis por gerar o token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Criar um usuário
    path('create_user/', views.create_user, name='create_user')
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # o endereço da imagem virá depois da url, passamos o endereço da pasta das imagens


# Usuario: tal
# senha: Tal123456
