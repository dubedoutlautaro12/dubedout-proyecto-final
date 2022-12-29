from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    
    def __str__(self):
      return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"

  
class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    dueno = models.CharField(max_length=200)
    peso = models.IntegerField()
    
    def __str__(self):
      return f"{self.nombre}, {self.peso}, {self.dueno}, {self.id}"


class Vehiculo(models.Model):
 dueno= models.CharField(max_length=100)
 tipo= models.CharField(max_length=100)
 patente =models.CharField(max_length=9)
 modelo = models.CharField(max_length=100)

 def __str__(self):
    return f"{self.dueno}, {self.tipo}, {self.patente}, {self.modelo} {self.id}"




