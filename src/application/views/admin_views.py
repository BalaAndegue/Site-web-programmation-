from django.shortcuts import render

from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
from ..models import Product, Order, CustomUser
from ..permissions import IsAdminUserCustom
from ..serializers import  OderSerializer, UserSerializer,ProductSerializer

class AdminProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUserCustom]

class AdminUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUserCustom]

class AdminOrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OderSerializer
    permission_classes = [IsAdminUserCustom]


# Create your views here.
