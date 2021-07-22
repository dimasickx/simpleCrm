import uuid

from django.db import models

# Create your models here.


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"id: {self.id}"
