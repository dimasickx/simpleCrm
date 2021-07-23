from django.test import TestCase
from .models import Order, Client, Employee

# Create your tests here.


class ClientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        client = Client.objects.create()
        employee = Employee.objects.create()
        Order.objects.create(type='CN', status='O', client=client, employee=employee)

    def test_str_method(self):
        order = Order.objects.get()
        expected = f"{order.type}, {order.status} {order.created_at}"
        self.assertEquals(expected, str(order))

