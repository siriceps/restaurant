# Generated by Django 2.2.4 on 2020-04-24 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycart', '0005_mycart_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='my_cart',
            field=models.ManyToManyField(null=True, to='mycart.MyCart'),
        ),
    ]
