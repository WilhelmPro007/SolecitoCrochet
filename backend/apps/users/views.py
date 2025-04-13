from django.views.generic import UpdateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User, ShippingAddress
from .serializers import UserSerializer, ShippingAddressSerializer
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import UserRegistrationForm

# API Views
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    @action(detail=False, methods=['get'])
    def profile(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    @action(detail=False, methods=['put'])
    def update_profile(self, request):
        user = request.user
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class ShippingAddressViewSet(viewsets.ModelViewSet):
    serializer_class = ShippingAddressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def set_default(self, request, pk=None):
        address = self.get_object()
        self.get_queryset().filter(is_default=True).update(is_default=False)
        address.is_default = True
        address.save()
        return Response({'status': 'Dirección establecida como predeterminada'})

# Template Views
class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'pages/users/profile.html'
    fields = ['first_name', 'last_name', 'email', 'phone_number']
    success_url = '/users/profile/'

    def get_object(self):
        return self.request.user

class AddressListView(LoginRequiredMixin, ListView):
    model = ShippingAddress
    template_name = 'pages/users/addresses.html'
    context_object_name = 'addresses'

    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user)

class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'pages/auth/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
