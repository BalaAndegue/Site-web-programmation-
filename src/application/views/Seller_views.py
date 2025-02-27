from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from ..models import Product
from ..permissions import IsVendor
from ..serializers import ProductSerializer

class SellerProductViewSet(viewsets.ModelViewSet):
    
    serializer_class = ProductSerializer
    permission_classes = [IsVendor]

    def get_queryset(self):
        return Product.objects.filter(seller=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(seller = self.request.user)
    
