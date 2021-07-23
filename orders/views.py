from django.shortcuts import render
from django.http import JsonResponse
from .models import Order
from .serializer import OrderSerializer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.


def get_orders(request):
    orders = Order.objects.all()
    serializer_orders = OrderSerializer(orders, many=True)
    return JsonResponse(serializer_orders.data, safe=False)
