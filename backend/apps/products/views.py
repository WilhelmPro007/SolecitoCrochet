from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django import forms

# Create your views here.

# Vista pública de productos
class ProductListView(ListView):
    model = Product
    template_name = 'pages/products/list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(is_active=True)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'pages/products/detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        return Product.objects.filter(is_active=True)

# Vista del dashboard de administración
@method_decorator(staff_member_required, name='dispatch')
class ProductAdminListView(ListView):
    model = Product
    template_name = 'pages/products/admin_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

# API ViewSets
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'category__name']
    ordering_fields = ['price', 'created_at', 'name']
    permission_classes = [IsAdminUser]  # Solo administradores pueden modificar productos

    def get_queryset(self):
        if self.request.user.is_staff:
            return Product.objects.all()
        return Product.objects.filter(is_active=True)

    @action(detail=False, methods=['GET'])
    def featured(self, request):
        featured_products = self.get_queryset().filter(is_active=True)[:6]
        serializer = self.get_serializer(featured_products, many=True)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes = [IsAdminUser]  # Solo administradores pueden modificar categorías

    @action(detail=True, methods=['GET'])
    def products(self, request, pk=None):
        category = self.get_object()
        products = Product.objects.filter(category=category, is_active=True)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

# Formulario para productos (si no existe uno personalizado)
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'stock', 'image', 'is_active']

# Dashboard: Crear producto
@method_decorator(staff_member_required, name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'pages/products/admin_form.html'
    success_url = reverse_lazy('products:admin_list')

# Dashboard: Editar producto
@method_decorator(staff_member_required, name='dispatch')
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'pages/products/admin_form.html'
    success_url = reverse_lazy('products:admin_list')

# Dashboard: Eliminar producto
@method_decorator(staff_member_required, name='dispatch')
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'pages/products/admin_confirm_delete.html'
    success_url = reverse_lazy('products:admin_list')
