# Generated by Django 3.1.7 on 2021-03-29 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wellness', '0009_remove_reminders_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminders',
            name='name',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]