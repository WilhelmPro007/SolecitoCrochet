from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='api_products')
router.register(r'categories', views.CategoryViewSet, basename='api_categories')

urlpatterns = [
    path('', include(router.urls)),
] 