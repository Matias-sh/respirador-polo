from django.db import models
from apps.doctores.models import Doctores
from apps.pacientes.models import Pacientes
# Create your models here.

class Datos_Respirador(models.Model):
    id_d_respirador = models.AutoField(primary_key=True)
    estado = models.BooleanField()
    id_doctor = models.ForeignKey(Doctores, on_delete=models.CASCADE)
    id_paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)