from django.db import models

# Create your models here.
class Owner(models.Model):
    nombre = models.CharField(max_length=25)
    edad =  models.IntegerField()
    pais =  models.CharField(max_length=27, default='')
    dni = models.CharField(max_length=8, default='00000000')
    vigente = models.BooleanField(default=True)

    def __str__(self):
      return (f"{self.nombre} de {self.pais} tiene {self.edad} años")