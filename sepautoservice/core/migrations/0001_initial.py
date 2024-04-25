# Generated by Django 5.0.4 on 2024-04-18 11:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Winkel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('adress', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Apointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sity', models.CharField(max_length=50)),
                ('postcode', models.CharField(max_length=6)),
                ('shipping_address', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('client', models.CharField(max_length=100)),
                ('telefon', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('winkel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.winkel')),
            ],
        ),
    ]
