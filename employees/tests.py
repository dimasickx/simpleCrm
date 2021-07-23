from django.test import TestCase
from .models import Employee

# Create your tests here.


class ClientModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Employee.objects.create(name='Sergei', surname='Sergeev', patronymic='Sergeevich')

    def test_name_label(self):
        employee = Employee.objects.get()
        field_label = employee._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        employee = Employee.objects.get()
        max_length = employee._meta.get_field('name').max_length
        self.assertEquals(max_length, 40)

    def test_surname_max_length(self):
        employee = Employee.objects.get()
        max_length = employee._meta.get_field('surname').max_length
        self.assertEquals(max_length, 40)

    def test_patronymic_max_length(self):
        employee = Employee.objects.get()
        max_length = employee._meta.get_field('patronymic').max_length
        self.assertEquals(max_length, 40)

    def test_str_method(self):
        employee = Employee.objects.get()
        expected = f"{employee.surname} {employee.name} {employee.patronymic}"
        self.assertEquals(expected, str(employee))
