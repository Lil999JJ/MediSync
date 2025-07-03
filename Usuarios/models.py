from django.db import models
from django.contrib.auth.models import AbstractUser

# --- Modelos de Soporte (Clínica) ---
# En un proyecto real, estos modelos estarían en su propia aplicación (ej. 'clinica')
# y se importarían aquí.

class Especialidad(models.Model):
    """Almacena las diferentes especialidades médicas."""
    # Django crea un campo 'id' como AutoField y primary_key por defecto.
    nombre = models.CharField(max_length=100, unique=True) 

    def __str__(self):
        return self.nombre

class Consultorio(models.Model):
    """Representa un consultorio físico en la clínica."""
    # Django crea un campo 'id' como AutoField y primary_key por defecto.
    nivel = models.CharField(max_length=50)
    numero_identificador = models.CharField(max_length=50, help_text="Ej: 'Piso 2, Puerta 5B'")

    def __str__(self):
        return self.numero_identificador


# --- Modelos Principales (Usuarios y Perfiles) ---

class Usuario(AbstractUser):
    """
    Modelo de Usuario personalizado. Gestiona el acceso al sistema, roles y 
    autenticación, extendiendo la funcionalidad base de Django.
    """
    class Rol(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        MEDICO = 'MEDICO', 'Médico'
        PACIENTE = 'PACIENTE', 'Paciente'
        SECRETARIA = 'SECRETARIA', 'Secretaria'

    # Campos de AbstractUser ya incluidos: username, first_name, last_name, email, password, etc.
    cedula = models.CharField(max_length=15, unique=True, help_text="Cédula de identidad del usuario.")
    rol = models.CharField(max_length=50, choices=Rol.choices, default=Rol.PACIENTE, help_text="Rol del usuario en el sistema.")

    # Previene conflictos con el modelo de usuario base de Django.
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_set',  # Nombre de acceso inverso único
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='usuario',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_set', # Nombre de acceso inverso único
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='usuario',
    )


class Paciente(models.Model):
    """Almacena la información del perfil de un paciente."""
    # Relación uno a uno que extiende el modelo Usuario. primary_key=True optimiza la relación.
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    # Nombre, Apellidos, Cédula y Email se obtienen del modelo Usuario.
    fecha_nacimiento = models.DateField(help_text="Fecha de nacimiento del paciente.")
    direccion = models.CharField(max_length=255, help_text="Dirección de residencia del paciente.")
    telefono = models.CharField(max_length=20, help_text="Número de teléfono de contacto del paciente.")
    genero = models.CharField(max_length=15, help_text="Género del paciente (ej. Masculino, Femenino).")
    nacionalidad = models.CharField(max_length=50, help_text="Nacionalidad del paciente.")
    
    def __str__(self):
        # Accede a los campos del modelo Usuario relacionado.
        return f"Paciente: {self.usuario.first_name} {self.usuario.last_name}"


class Medico(models.Model):
    """Contiene la información del perfil de un médico."""
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    # Información personal (nombre, cédula, email) se hereda de Usuario.
    tarifa_consulta = models.DecimalField(max_digits=10, decimal_places=2, help_text="Costo de la consulta con el médico.")
    especialidad = models.ForeignKey(Especialidad, on_delete=models.SET_NULL, null=True, help_text="Especialidad del médico.")
    consultorio = models.ForeignKey(Consultorio, on_delete=models.SET_NULL, null=True, help_text="Consultorio asignado al médico.")

    def __str__(self):
        return f"Dr. {self.usuario.first_name} {self.usuario.last_name}"


class Secretaria(models.Model):
    """Almacena la información del perfil del personal de secretaría."""
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    # Información personal (nombre, cédula, email) se hereda de Usuario.
    medico_asociado = models.ForeignKey(Medico, on_delete=models.SET_NULL, null=True, blank=True, help_text="Médico al que asiste la secretaria.")

    def __str__(self):
        return f"Secretaria: {self.usuario.first_name} {self.usuario.last_name}"