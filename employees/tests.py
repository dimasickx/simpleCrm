from django.test import TestCase
from .models import Employee

# Create your tests here.


# class ClientModelTest(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         # Set up non-modified objects used by all test methods
#         Employee.objects.create(telegram_id='@client')
#
#     def test_telegram_id_label(self):
#         employee = Employee.objects.get()
#         field_label = employee._meta.get_field('telegram_id').verbose_name
#         self.assertEquals(field_label, 'telegram id')
#
#     def test_telegram_id_max_length(self):
#         employee = Employee.objects.get()
#         max_length = employee._meta.get_field('telegram_id').max_length
#         self.assertEquals(max_length, 40)
#
#     def test_str_method(self):
#         employee = Employee.objects.get()
#         expected = f'id: {employee.id}'
#         self.assertEquals(expected, str(employee))
