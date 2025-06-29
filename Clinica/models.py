from django.db import models
from Usuarios.models import Medico

class Especialidad(models.Model):
    """
    Catálogo de las especialidades médicas disponibles en la clínica.
    Fuente: Tabla Especialidad, p. 33
    """
    # ID_Especialidad es el 'id' automático de Django.
    ID_Especialidad = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100, help_text="Nombre de la especialidad (ej. Cardiología).") #

    def __str__(self):
        return self.Nombre

class Consultorio(models.Model):
    """
    Catálogo de los consultorios físicos de la clínica.
    Fuente: Tabla Consultorio, p. 33
    """
    # ID_Consultorio es el 'id' automático de Django.
    ID_Consultorio = models.AutoField(primary_key=True)
    Nivel = models.CharField(max_length=50, help_text="Ubicación o nivel del consultorio.") #

    def __str__(self):
        return f"Consultorio {self.Nivel}"

class HorarioMedico(models.Model):
    """
    Modelo para gestionar los horarios disponibles de cada médico.
    Este modelo es una implementación lógica basada en la funcionalidad
    "Gestionar Horarios Médicos" (p. 23).
    """
    class DiaSemana(models.TextChoices):
        LUNES = 'LUN', 'Lunes'
        MARTES = 'MAR', 'Martes'
        MIERCOLES = 'MIE', 'Miércoles'
        JUEVES = 'JUE', 'Jueves'
        VIERNES = 'VIE', 'Viernes'
        SABADO = 'SAB', 'Sábado'
        DOMINGO = 'DOM', 'Domingo'

    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name="horarios")
    dia = models.CharField(max_length=3, choices=DiaSemana.choices)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    class Meta:
        # Se asegura que un médico no pueda tener dos horarios que se solapen en el mismo día.
        unique_together = ('medico', 'dia', 'hora_inicio', 'hora_fin')

    def __str__(self):
        return f"{self.medico} - {self.get_dia_display()}: {self.hora_inicio.strftime('%I:%M %p')} - {self.hora_fin.strftime('%I:%M %p')}"
