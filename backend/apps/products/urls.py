from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # URLs públicas
    path('', views.ProductListView.as_view(), name='list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    
    # URL del dashboard de administración (ahora solo necesitamos una vista)
    path('admin/', views.ProductAdminListView.as_view(), name='admin_list'),
] 