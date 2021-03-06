# Generated by Django 2.2.4 on 2020-03-17 03:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0003_auto_20200310_1710'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_order', models.DateTimeField(blank=True, default=datetime.datetime.now, editable=False)),
                ('service_charge', models.FloatField(default=0)),
                ('vat', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('is_paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-datetime_order'],
            },
        ),
        migrations.CreateModel(
            name='MyCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.SmallIntegerField(default=1)),
                ('datetime_create', models.DateTimeField(blank=True, default=datetime.datetime.now, editable=False)),
                ('food_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Menu')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycart.Order')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['datetime_create'],
            },
        ),
    ]
