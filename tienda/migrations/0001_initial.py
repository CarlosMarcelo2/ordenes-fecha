# Generated by Django 4.2.4 on 2023-08-11 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=128)),
                ('direccion', models.CharField(max_length=256)),
                ('fecha', models.DateField()),
                ('fecha_envio', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('descripcion', models.CharField(max_length=128)),
                ('precio', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('precio', models.PositiveIntegerField()),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tienda.orden')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tienda.producto')),
            ],
        ),
    ]
