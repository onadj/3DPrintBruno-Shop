# Generated by Django 4.2.7 on 2023-11-29 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20210308_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
