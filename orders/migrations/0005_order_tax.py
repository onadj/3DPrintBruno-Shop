# Generated by Django 3.1 on 2023-11-08 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_remove_order_tax'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tax',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
