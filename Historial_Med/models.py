from django.db import models

# Se asume que el modelo Paciente existe en la aplicación 'usuarios'.
from Usuarios.models import Paciente

class HistorialMedico(models.Model):
    """
    Contiene el registro de todos los diagnósticos y tratamientos
    que ha recibido un paciente.
    Fuente: Tabla Historial Medico, p. 27
    """
    ID_Hist_med = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        related_name="historiales",
        help_text="Referencia al paciente (Paciente.ID_Paciente)."
    ) #
    fecha = models.DateField(help_text="Fecha en que se realizó el diagnóstico.") #
    diagnostico = models.TextField(help_text="Descripción del diagnóstico médico.") #
    tratamiento = models.TextField(help_text="Tratamiento prescrito para el diagnóstico.") #
    observaciones = models.TextField(help_text="Observaciones adicionales del médico.", blank=True, null=True) #
    medicamentos = models.TextField(help_text="Medicamentos recetados al paciente.", blank=True, null=True) #

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f"Registro de {self.paciente} - {self.fecha}"

class SeguroMedico(models.Model):
    """
    Almacena la información del seguro médico de cada paciente.
    Fuente: Tabla Seguro_Med, p. 28
    """
    ID_Seg = models.AutoField(primary_key=True)
    paciente = models.OneToOneField(
        Paciente,
        on_delete=models.CASCADE,
        related_name="seguro",
        help_text="Paciente asegurado."
    )
    # El campo Cedula se obtiene del paciente vinculado.
    nombre = models.CharField(max_length=100, help_text="Nombre de la compañía de seguros.") #
    cobertura = models.TextField(help_text="Descripción de la cobertura del seguro.") #
    telefono = models.CharField(max_length=20, help_text="Teléfono de contacto de la aseguradora.") #
    email = models.EmailField(max_length=100, help_text="Correo electrónico de la aseguradora.", blank=True) #

    def __str__(self):
        return f"Seguro de {self.paciente}: {self.nombre}"
