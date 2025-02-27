from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.admin_views import AdminProductViewSet, AdminOrderViewSet
from .views.Custom_views import user_dashboard
from .views.Seller_views import SellerProductViewSet

router = DefaultRouter()
router.register(r'admin/products', AdminProductViewSet, basename='adminproduct')
router.register(r'admin/orders',AdminOrderViewSet, basename='order')
router.register(r'vendor/products', SellerProductViewSet,basename='sellerproduct')

urlpatterns = [
    path('api/',include(router.urls)),
    path('api/user/dashboard',user_dashboard),
]