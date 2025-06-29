from django.db import models
from django.contrib.auth.models import AbstractUser

# Se asume que los siguientes modelos existen en una aplicación llamada 'clinica'
# from clinica.models import Especialidad, Consultorio

# Para mantener el ejemplo autocontenido, se definen aquí temporalmente.
# En el proyecto real, estas clases estarían en clinica/models.py y se importarían.
class Especialidad(models.Model):
    ID_Especialidad = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100) 

    def __str__(self):
        return self.Nombre

class Consultorio(models.Model):
    ID_Consultorio = models.AutoField(primary_key=True)
    Nivel = models.CharField(max_length=50)

    def __str__(self):
        return self.Nivel

class Usuario(AbstractUser):
    """
    Modelo de Usuario personalizado que extiende el de Django.
    Gestiona el acceso al sistema, roles y autenticación.
    """
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        MEDICO = 'MEDICO', 'Médico'
        PACIENTE = 'PACIENTE', 'Paciente'
        SECRETARIA = 'SECRETARIA', 'Secretaria'

    # El campo 'Apellidos' se maneja con 'last_name' de AbstractUser.
    # El campo 'Contraseña' es manejado por Django ('password').
    # El campo 'ID_Usuario' es el 'id' automático de Django.
    cedula = models.CharField(max_length=15, unique=True, help_text="Cédula asociada a la cuenta de usuario.") # [cite: 201]
    roll = models.CharField(max_length=50, choices=Role.choices, help_text="Rol del usuario en el sistema.") # [cite: 201]

class Paciente(models.Model):
    """
    [cite_start]Almacena la información personal de cada paciente. [cite: 172]
    """
    # ID_Paciente es el 'id' automático de Django. Se crea una relación uno a uno con el usuario.
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    # Nombre y Apellidos se obtienen del modelo Usuario vinculado.
    fecha_nacimiento = models.DateField(help_text="Fecha de nacimiento del paciente.") # [cite: 173]
    direccion = models.CharField(max_length=255, help_text="Dirección de residencia del paciente.") # [cite: 173]
    telefono = models.CharField(max_length=20, help_text="Número de teléfono de contacto del paciente.") # [cite: 173]
    # E-Mail se obtiene del modelo Usuario.
    genero = models.CharField(max_length=15, help_text="Género del paciente.") # [cite: 173]
    nacionalidad = models.CharField(max_length=50, help_text="Nacionalidad del paciente.") # [cite: 173]
    
    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name}"

class Medico(models.Model):
    """
    [cite_start]Contiene la información de los médicos que trabajan en la clínica. [cite: 192]
    """
    # ID_Medico es el 'id' automático de Django. Se crea una relación uno a uno con el usuario.
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    # Nombre, Apellidos, Cedula, Telefono y E-Mail se obtienen del modelo Usuario.
    tarifa_cons = models.DecimalField(max_digits=10, decimal_places=2, help_text="Costo de la consulta con el médico.") # [cite: 193]
    id_especialidad = models.ForeignKey(Especialidad, on_delete=models.SET_NULL, null=True, help_text="Referencia a la especialidad del médico.") # [cite: 193]
    id_consultorio = models.ForeignKey(Consultorio, on_delete=models.SET_NULL, null=True, help_text="Referencia al consultorio del médico.") # [cite: 193]

    def __str__(self):
        return f"Dr. {self.usuario.first_name} {self.usuario.last_name}"

class Secretaria(models.Model):
    """
    [cite_start]Almacena la información del personal de secretaría. [cite: 189]
    """
    # ID_Secre es el 'id' automático de Django. Se crea una relación uno a uno con el usuario.
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    # Nombre, Apellido, Cedula, Telefono y E-Mail se obtienen del modelo Usuario.
    id_medico = models.ForeignKey(Medico, on_delete=models.CASCADE, help_text="Referencia al médico que asiste.") # [cite: 190]

    def __str__(self):
        return f"Secretaria: {self.usuario.first_name} {self.usuario.last_name}"
