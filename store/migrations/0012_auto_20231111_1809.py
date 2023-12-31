# Generated by Django 3.1 on 2023-11-11 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_productvideo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productvideo',
            options={},
        ),
        migrations.AlterField(
            model_name='productvideo',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='store.product'),
        ),
        migrations.AlterField(
            model_name='productvideo',
            name='video',
            field=models.FileField(upload_to='store/products/videos'),
        ),
    ]
