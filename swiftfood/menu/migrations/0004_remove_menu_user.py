# Generated by Django 2.2.4 on 2020-03-19 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20200310_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='user',
        ),
    ]
