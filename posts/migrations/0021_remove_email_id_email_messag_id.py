# Generated by Django 4.1.7 on 2023-03-18 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0020_rename_to_email_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='id',
        ),
        migrations.AddField(
            model_name='email',
            name='messag_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
