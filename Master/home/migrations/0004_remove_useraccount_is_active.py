# Generated by Django 4.2 on 2023-05-21 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_useraccount_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='is_active',
        ),
    ]
