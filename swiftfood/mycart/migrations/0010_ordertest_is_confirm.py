# Generated by Django 2.2.4 on 2020-04-26 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycart', '0009_auto_20200426_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordertest',
            name='is_confirm',
            field=models.BooleanField(default=False),
        ),
    ]