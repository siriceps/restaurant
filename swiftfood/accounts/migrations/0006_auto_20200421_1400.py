# Generated by Django 2.2.4 on 2020-04-21 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_delete_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
