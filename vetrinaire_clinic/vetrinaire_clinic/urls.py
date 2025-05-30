
#Ajouter les endpoints d’authentification
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('owners.urls')),
    path('', include('patients.urls')),
    path('auth/', include('accounts.urls')),
    path('auth/login/', obtain_auth_token),  # Endpoint pour obtenir un token
]
