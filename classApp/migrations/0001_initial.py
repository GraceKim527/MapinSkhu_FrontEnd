# Generated by Django 4.1.6 on 2023-02-20 06:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50)),
                ('class_name', models.CharField(max_length=300)),
                ('prof', models.CharField(max_length=100)),
                ('room', models.CharField(max_length=100, null=True)),
                ('date1', models.CharField(max_length=5, null=True)),
                ('date2', models.CharField(max_length=5, null=True)),
                ('start', models.TimeField(max_length=10, null=True)),
                ('end', models.TimeField(max_length=10, null=True)),
                ('kwan_name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kwan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kwan_num', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(13)])),
                ('kwan_name', models.CharField(max_length=50, null=True)),
                ('kwan_image', models.ImageField(blank=True, null=True, upload_to='images/kwan')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kwan_name', models.CharField(max_length=50)),
                ('room', models.CharField(max_length=100)),
                ('floor', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('room_image', models.ImageField(blank=True, null=True, upload_to='images/room')),
                ('room_type', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
