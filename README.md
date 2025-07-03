Migraciones codigos de control


Migrations for 'Citas':
  Citas\migrations\0001_initial.py
    + Create model Cita
  Citas\migrations\0002_initial.py
    + Add field medico to cita
    + Add field paciente to cita
    ~ Alter unique_together for cita (1 constraint(s))
Migrations for 'Facturacion':
  Facturacion\migrations\0001_initial.py
    + Create model Pago
Migrations for 'Clinica':
  Clinica\migrations\0001_initial.py
    + Create model Consultorio
    + Create model Especialidad
    + Create model HorarioMedico
  Clinica\migrations\0002_initial.py
    + Add field medico to horariomedico
    ~ Alter unique_together for horariomedico (1 constraint(s))
Migrations for 'Historial_Med':
  Historial_Med\migrations\0001_initial.py
    + Create model HistorialMedico
    + Create model SeguroMedico
  Historial_Med\migrations\0002_initial.py
    + Add field paciente to historialmedico
    + Add field paciente to seguromedico
Migrations for 'Usuarios':
  Usuarios\migrations\0001_initial.py
    + Create model Consultorio
    + Create model Especialidad
    + Create model Usuario
    + Create model Paciente
    + Create model Medico
    + Create model Secretaria
