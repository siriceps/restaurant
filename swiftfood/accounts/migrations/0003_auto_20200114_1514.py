# Generated by Django 2.2.4 on 2020-01-14 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='point',
            field=models.SmallIntegerField(default=0),
        ),
    ]
