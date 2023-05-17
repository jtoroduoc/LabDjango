# Generated by Django 4.2.1 on 2023-05-17 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('ppu', models.CharField(max_length=6, primary_key=True, serialize=False, unique=True, verbose_name='Patente')),
                ('marca', models.CharField(max_length=10, verbose_name='Marca')),
                ('modelo', models.CharField(max_length=10, verbose_name='Modelo')),
                ('año', models.IntegerField(verbose_name='Año')),
            ],
        ),
    ]