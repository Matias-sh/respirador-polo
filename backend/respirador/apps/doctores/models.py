from django.db import models
from apps.personas.models import Personas

# Create your models here.

class Especialidad(models.Model):
    id_especialidad = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=70)

class Doctores(models.Model):
    id_doctor = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(Personas, on_delete=models.CASCADE)
    id_especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
