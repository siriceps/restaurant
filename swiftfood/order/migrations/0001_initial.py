# Generated by Django 2.2.4 on 2020-02-11 11:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.SmallIntegerField(default=1)),
                ('datetime', models.DateTimeField(blank=True, default=datetime.datetime.now, editable=False)),
                ('is_confirm', models.BooleanField(default=True)),
                ('service_charge', models.SmallIntegerField(default=0)),
                ('vat', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('food_menu', models.ManyToManyField(to='menu.Menu')),
            ],
        ),
    ]
