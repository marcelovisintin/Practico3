from django.db import models

class Maquina (models.Model):
    marca = models.CharField(max_length=40)
    proceso= models.CharField(max_length=40)
    descripcion = models.TextField()

    def __str__(self):
        return f'Maquina({self.id}): {self.marca} - Proceso: {self.proceso} - Descripcion: {self.descripcion}'
