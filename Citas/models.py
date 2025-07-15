from django.db import models
from Usuarios.models import Paciente, Medico

class Cita(models.Model):
    """
    Registra la información de las citas médicas programadas,
    vinculando a un paciente con un médico en una fecha y hora específicas.
    Este modelo combina la información de las tablas Cita y Paciente_Cita
    descritas en el documento (p. 29).
    """
    class EstadoCita(models.TextChoices):
        PROGRAMADA = 'PROGRAMADA', 'Programada'
        CONFIRMADA = 'CONFIRMADA', 'Confirmada'
        CANCELADA = 'CANCELADA', 'Cancelada'
        COMPLETADA = 'COMPLETADA', 'Completada'

    # ID_Cita es el 'id' automático de Django.
    # La tabla intermedia Paciente_Cita se representa con las siguientes dos llaves foráneas.
    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        help_text="Referencia al paciente que solicita la cita."
    ) #
    medico = models.ForeignKey(
        Medico,
        on_delete=models.CASCADE,
        help_text="Referencia al médico asignado a la cita."
    ) #

    # Campos de la tabla Cita
    fecha = models.DateField(help_text="Fecha programada para la cita.") 
    hora = models.TimeField(help_text="Hora programada para la cita.") 
    # Campo adicional para gestionar el flujo de la cita.
    estado = models.CharField(
        max_length=20,
        choices=EstadoCita.choices,
        default=EstadoCita.PROGRAMADA,
        help_text="El estado actual de la cita."
    )

    class Meta:
        # Se asegura que un médico no pueda tener dos citas a la misma hora y en la misma fecha.
        unique_together = ('medico', 'fecha', 'hora')
        ordering = ['fecha', 'hora']

    def __str__(self):
        return f"Cita de {self.paciente} con {self.medico} el {self.fecha} a las {self.hora.strftime('%I:%M %p')}"