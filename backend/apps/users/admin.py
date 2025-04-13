from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, ShippingAddress

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Información adicional', {'fields': ('phone_number', 'address')}),
    )

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'state', 'is_default')
    list_filter = ('city', 'state', 'is_default')
    search_fields = ('user__email', 'address', 'city')
