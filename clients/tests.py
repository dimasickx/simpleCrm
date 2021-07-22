from django.test import TestCase
from .models import Client

# Create your tests here.


class ClientModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Client.objects.create(telegram_id='@client')

    def test_telegram_id_label(self):
        client = Client.objects.get()
        field_label = client._meta.get_field('telegram_id').verbose_name
        self.assertEquals(field_label, 'telegram id')

    def test_telegram_id_max_length(self):
        client = Client.objects.get()
        max_length = client._meta.get_field('telegram_id').max_length
        self.assertEquals(max_length, 40)

    def test_str_method(self):
        client = Client.objects.get()
        expected = f'id: {client.id}'
        self.assertEquals(expected, str(client))
