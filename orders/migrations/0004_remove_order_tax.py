# Generated by Django 3.1 on 2023-11-08 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210313_0218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tax',
        ),
    ]
