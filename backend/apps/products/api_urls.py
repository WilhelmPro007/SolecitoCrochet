from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='product-api')
router.register(r'categories', views.CategoryViewSet, basename='category-api')

urlpatterns = [
    path('', include(router.urls)),
] 