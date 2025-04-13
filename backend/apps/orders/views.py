from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# API Views
class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def cancel_order(self, request, pk=None):
        order = self.get_object()
        if order.status == 'pending':
            order.status = 'cancelled'
            order.save()
            return Response({'status': 'Orden cancelada'})
        return Response(
            {'error': 'No se puede cancelar esta orden'}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    @action(detail=False, methods=['get'])
    def summary(self, request):
        orders = self.get_queryset()
        total_orders = orders.count()
        total_spent = orders.aggregate(total=Sum('total_amount'))['total'] or 0
        
        status_summary = {
            status: orders.filter(status=status).count()
            for status, _ in Order.STATUS_CHOICES
        }

        return Response({
            'total_orders': total_orders,
            'total_spent': total_spent,
            'status_summary': status_summary
        })

# Template Views
class CartView(TemplateView):
    template_name = 'pages/orders/cart.html'

class CheckoutView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/orders/checkout.html'

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'pages/orders/list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'pages/orders/detail.html'
    context_object_name = 'order'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
