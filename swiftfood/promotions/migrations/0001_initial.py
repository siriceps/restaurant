# Generated by Django 2.2.4 on 2020-02-11 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promotion_name', models.CharField(blank=True, db_index=True, max_length=50)),
                ('promotion_code', models.CharField(blank=True, db_index=True, max_length=50)),
                ('promotion_picture', models.ImageField(blank=True, null=True, upload_to='promotions/%Y/%m/')),
                ('description', models.CharField(blank=True, db_index=True, max_length=50)),
                ('discount', models.FloatField(default=0)),
                ('promotion_order', models.ManyToManyField(to='order.OrderMenu')),
            ],
        ),
    ]
