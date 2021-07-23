from django.shortcuts import render
from django.http import JsonResponse
from .models import Order
from .serializer import OrderSerializer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.


# @api_view(['GET', 'POST'])
# def get_orders(request):
#     if request.method == 'GET':
#         orders = Order.objects.all()
#         serializer_orders = OrderSerializer(orders, many=True)
#         return JsonResponse(serializer_orders.data, safe=False)
#     elif request.method == 'POST':
#         order_data = JSONParser().parse(request)
#         order_serialize = OrderSerializer(data=order_data)
#         if order_serialize.is_valid():
#             order_serialize.save()
#             return JsonResponse(order_serialize.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(order_serialize.errors, status=status.HTTP_400_BAD_REQUEST)
