# Generated by Django 4.2.7 on 2023-11-29 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_about_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='aboutimage',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
