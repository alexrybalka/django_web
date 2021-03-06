# Generated by Django 2.1 on 2018-08-22 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(default='Add some description', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='VehiclePart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField(default='Add some description', max_length=1000)),
                ('pub_date', models.DateTimeField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_car.Section')),
            ],
        ),
    ]
