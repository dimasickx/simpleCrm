from django.shortcuts import render
from django.http import JsonResponse
from .models import Client
from .serializer import ClientSerializer

# Create your views here.


def get_clients(request):
    clients = Client.objects.all()
    serializer_clients = ClientSerializer(clients, many=True)
    return JsonResponse(serializer_clients.data, safe=False)
