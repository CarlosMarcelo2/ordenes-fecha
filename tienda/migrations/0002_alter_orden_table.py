# Generated by Django 4.2.4 on 2023-08-11 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='orden',
            table='tienda_order',
        ),
    ]