"""
URL configuration for SolecitoCrochet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from apps.users.views import RegisterView

# Definir patrones de URL para la API
api_patterns = [
    path('products/', include('apps.products.api_urls')),
    path('orders/', include('apps.orders.api_urls')),
    path('users/', include('apps.users.api_urls')),
    path('auth/', include('rest_framework.urls')),
]

# Definir patrones de URL principales
urlpatterns = [
    # URLs de administración
    path('admin/', admin.site.urls),
    
    # URLs de autenticación
    path('auth/', include([
        path('login/', auth_views.LoginView.as_view(template_name='pages/auth/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
        path('register/', RegisterView.as_view(), name='register'),
    ])),
    
    # URLs de la API
    path('api/v1/', include(api_patterns)),
    
    # URLs del frontend
    path('', TemplateView.as_view(template_name='pages/home/landing.html'), name='home'),
    path('products/', include('apps.products.urls', namespace='products')),
    path('orders/', include('apps.orders.urls', namespace='orders')),
    path('users/', include('apps.users.urls', namespace='users')),
]

# Servir archivos media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
