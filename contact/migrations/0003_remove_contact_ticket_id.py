# Generated by Django 3.1 on 2023-11-25 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20231125_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='ticket_id',
        ),
    ]