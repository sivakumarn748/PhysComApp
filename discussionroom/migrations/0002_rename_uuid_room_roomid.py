# Generated by Django 5.0.7 on 2024-08-04 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discussionroom', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='uuid',
            new_name='roomid',
        ),
    ]
