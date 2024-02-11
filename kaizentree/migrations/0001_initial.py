# Generated by Django 4.1.13 on 2024-02-11 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('in_stock', models.BooleanField()),
                ('available_stock', models.IntegerField()),
            ],
        ),
    ]
