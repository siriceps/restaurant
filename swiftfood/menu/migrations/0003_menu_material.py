# Generated by Django 2.2.4 on 2020-02-11 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
        ('menu', '0002_auto_20200211_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='material',
            field=models.ManyToManyField(to='stock.Stock'),
        ),
    ]