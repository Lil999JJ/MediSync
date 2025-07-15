from django.contrib import admin
from .models import Especialidad, Consultorio, Medico, Usuario, Paciente, Secretaria

admin.site.register(Especialidad)
admin.site.register(Consultorio)        
admin.site.register(Medico)
admin.site.register(Usuario)
admin.site.register(Paciente)
admin.site.register(Secretaria)

# Register your models here.
