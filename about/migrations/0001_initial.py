# Generated by Django 3.1 on 2023-11-09 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='about/images/')),
                ('video_url', models.URLField(blank=True)),
            ],
        ),
    ]
