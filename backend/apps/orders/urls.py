from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('my-orders/', views.OrderListView.as_view(), name='list'),
    path('my-orders/<int:pk>/', views.OrderDetailView.as_view(), name='detail'),
] 