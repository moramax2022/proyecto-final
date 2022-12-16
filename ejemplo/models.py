from django.db import models


# Create your models here.
from django.db import models
class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    def __str__(self):
      return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"

from django.db import models
class Alumnos(models.Model):
    nombre = models.CharField(max_length=50)
    curso = models.CharField(max_length=50)
    numero_matricula = models.IntegerField()
    def __str__(self):
      return f"{self.nombre},{self.curso} {self.numero_matricula}, {self.id}"

from django.db import models
class Docentes(models.Model):
    nombre = models.CharField(max_length=50)
    asignatura= models.CharField(max_length=50)
    grado = models.IntegerField()
    def __str__(self):
      return f"{self.nombre},{self.asignatura} {self.grado}, {self.id}"
      