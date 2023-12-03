from django.db import models

# Create your models here.
class Pokemon(models.Model):
    nombre = models.CharField(max_length=25)
    pais = models.CharField(max_length=10)
    descripcion = models.TextField()