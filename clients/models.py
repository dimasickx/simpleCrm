import uuid

from django.db import models

# Create your models here.


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    patronymic = models.CharField(max_length=40)

    telegram_id = models.CharField(max_length=40)

    def __str__(self):
        return f"id: {self.id}"
