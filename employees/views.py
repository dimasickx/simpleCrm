from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
from .serializer import EmployeeSerializer

# Create your views here.


def get_employees(request):
    employees = Employee.objects.all()
    serializer_employees = EmployeeSerializer(employees, many=True)
    return JsonResponse(serializer_employees.data, safe=False)
