from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from ..models import Order
from ..permissions import IsUserCustom
from ..serializers import  OderSerializer

@api_view(['GET'])
@permission_classes([IsUserCustom])
def user_dashboard(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    return Response({
        "username": user.username,
        "role":user.role,
        "orders":OderSerializer(orders, many=True).data
    })