
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # URL para a interface administrativa
    path('api/', include('api.urls'))  # Incluindo URLs da aplicação 'api'
]
