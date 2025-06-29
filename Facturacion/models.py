from django.db import models

# Se asume que el modelo Cita existe en la aplicación 'citas'.
from Citas.models import Cita

class Pago(models.Model):
    """
    Registra los pagos realizados por las citas o servicios.
    Permite generar facturas simples y consultar un historial de transacciones.
    Fuente: Tabla Pago, p. 30
    """
    ID_Pago = models.AutoField(primary_key=True, help_text="Identificador único del pago.") #
    cita = models.OneToOneField(
        Cita,
        on_delete=models.CASCADE,
        related_name="pago",
        help_text="Referencia a la cita asociada al pago (Cita.ID_Cita)."
    ) #
    monto = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Cantidad total del pago."
    ) #
    fecha_pago = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha y hora en que se realizó el pago."
    ) #
    metodo_pago = models.CharField(
        max_length=50,
        help_text="Método utilizado para el pago (ej. Efectivo, TC)."
    ) #
    estado = models.CharField(
        max_length=20,
        help_text="Estado del pago (ej. Completado, Pendiente)."
    ) #

    def __str__(self):
        return f"Pago de {self.monto} para la {self.cita}"
