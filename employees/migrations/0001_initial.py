# Generated by Django 2.2.10 on 2021-07-23 07:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('surname', models.CharField(max_length=40)),
                ('patronymic', models.CharField(max_length=40)),
                ('position', models.CharField(max_length=60)),
            ],
        ),
    ]
