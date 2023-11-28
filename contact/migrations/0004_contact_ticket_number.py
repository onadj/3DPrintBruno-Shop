# Generated by Django 3.1 on 2023-11-25 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_remove_contact_ticket_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='ticket_number',
            field=models.CharField(default='DEFAULT_TICKET', editable=False, max_length=16, unique=True),
        ),
    ]