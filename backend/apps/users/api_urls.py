from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user-api')
router.register(r'shipping-addresses', views.ShippingAddressViewSet, basename='address-api')

urlpatterns = router.urls 