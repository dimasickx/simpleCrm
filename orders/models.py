import uuid

from django.db import models
from clients.models import Client
from employees.models import Employee

# Create your models here.


class Order(models.Model):
    choice_type = [('RPR', 'Ремонт'), ('SRVC', 'Обслуживание'), ('CN', 'Консультация')]
    choice_status = [('O', 'Открыта'), ('P', 'В работе'), ('C', 'Закрыта')]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=30, choices=choice_type)
    status = models.CharField(max_length=30, choices=choice_status)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employees = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"id: {self.id}"
