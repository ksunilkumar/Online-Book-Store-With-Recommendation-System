# Generated by Django 2.2.1 on 2019-09-17 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20190917_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='phone_number',
        ),
    ]
