# Generated by Django 4.0.4 on 2023-03-18 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0023_remove_email_message_id_email_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='to',
            field=models.EmailField(max_length=255),
        ),
    ]
