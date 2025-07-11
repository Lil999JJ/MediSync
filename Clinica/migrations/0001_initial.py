# Generated by Django 5.2.3 on 2025-07-03 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consultorio',
            fields=[
                ('ID_Consultorio', models.AutoField(primary_key=True, serialize=False)),
                ('Nivel', models.CharField(help_text='Ubicación o nivel del consultorio.', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('ID_Especialidad', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(help_text='Nombre de la especialidad (ej. Cardiología).', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HorarioMedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(choices=[('LUN', 'Lunes'), ('MAR', 'Martes'), ('MIE', 'Miércoles'), ('JUE', 'Jueves'), ('VIE', 'Viernes'), ('SAB', 'Sábado'), ('DOM', 'Domingo')], max_length=3)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
            ],
        ),
    ]
