# Generated by Django 3.1.7 on 2021-03-23 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wellness', '0002_auto_20210323_0953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['user']},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='eligible',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='points',
        ),
    ]