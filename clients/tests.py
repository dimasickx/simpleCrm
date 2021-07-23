from django.test import TestCase
from .models import Client

# Create your tests here.


class ClientModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Client.objects.create(name='Ivan', surname='Ivanov', patronymic='Ivanovich', telegram_id='@client')

    def test_telegram_id_label(self):
        client = Client.objects.get()
        field_label = client._meta.get_field('telegram_id').verbose_name
        self.assertEquals(field_label, 'telegram id')

    def test_telegram_id_max_length(self):
        client = Client.objects.get()
        max_length = client._meta.get_field('telegram_id').max_length
        self.assertEquals(max_length, 40)

    def test_name_max_length(self):
        client = Client.objects.get()
        max_length = client._meta.get_field('name').max_length
        self.assertEquals(max_length, 40)

    def test_surname_max_length(self):
        client = Client.objects.get()
        max_length = client._meta.get_field('surname').max_length
        self.assertEquals(max_length, 40)

    def test_patronymic_max_length(self):
        client = Client.objects.get()
        max_length = client._meta.get_field('patronymic').max_length
        self.assertEquals(max_length, 40)

    def test_str_method(self):
        client = Client.objects.get()
        expected = f"{client.surname} {client.name} {client.patronymic}"
        self.assertEquals(expected, str(client))
