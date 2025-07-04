# Generated by Django 5.2.3 on 2025-07-03 13:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Citas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('ID_Pago', models.AutoField(help_text='Identificador único del pago.', primary_key=True, serialize=False)),
                ('monto', models.DecimalField(decimal_places=2, help_text='Cantidad total del pago.', max_digits=10)),
                ('fecha_pago', models.DateTimeField(auto_now_add=True, help_text='Fecha y hora en que se realizó el pago.')),
                ('metodo_pago', models.CharField(help_text='Método utilizado para el pago (ej. Efectivo, TC).', max_length=50)),
                ('estado', models.CharField(help_text='Estado del pago (ej. Completado, Pendiente).', max_length=20)),
                ('cita', models.OneToOneField(help_text='Referencia a la cita asociada al pago (Cita.ID_Cita).', on_delete=django.db.models.deletion.CASCADE, related_name='pago', to='Citas.cita')),
            ],
        ),
    ]
