# Generated by Django 2.2.4 on 2020-01-28 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermenu',
            name='food_menu',
        ),
        migrations.AddField(
            model_name='ordermenu',
            name='food_menu',
            field=models.ManyToManyField(to='menu.Menu'),
        ),
    ]