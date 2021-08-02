import uuid

from django.db import models
from clients.models import Client
from employees.models import Employee

from django.db.models.signals import pre_save
from django.dispatch import receiver

import requests

# Create your models here.

token = '1939870399:AAGtbP_G7iEVl3EvDxIkpr83v2qAz_fyLuo'


class Order(models.Model):
    choice_type = [('RPR', 'Ремонт'), ('SRVC', 'Обслуживание'), ('CN', 'Консультация')]
    choice_status = [('O', 'Открыта'), ('P', 'В работе'), ('C', 'Закрыта')]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=30, choices=choice_type)
    status = models.CharField(max_length=30, choices=choice_status)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type}, {self.status} {self.created_at}"


@receiver(pre_save, sender=Order)
def send_msg(sender, **kwargs):
    order = kwargs['instance']
    client = Client.objects.filter(order__id=order.id).first()
    if client is not None:
        chat_id = client.telegram_id
        requests.get(f'https://api.telegram.org/bot{token}/'
                     f'sendMessage?chat_id={chat_id}&text=статус заявки изменен на {order.get_status_display()}')


pre_save.connect(send_msg, Order.status, dispatch_uid="my_unique_identifier")
