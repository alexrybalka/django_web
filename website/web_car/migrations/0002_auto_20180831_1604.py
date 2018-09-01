# Generated by Django 2.1 on 2018-08-31 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_car', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclepart',
            name='price',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=15),
        ),
        migrations.AlterField(
            model_name='vehiclepart',
            name='pub_date',
            field=models.DateTimeField(default='2018-08-31 16:04'),
        ),
    ]
