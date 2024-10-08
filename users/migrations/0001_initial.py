# Generated by Django 5.0.7 on 2024-08-03 13:27

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=16)),
                ('sessid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
