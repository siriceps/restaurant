# Generated by Django 2.2.4 on 2020-04-21 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycart', '0004_auto_20200420_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycart',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]
