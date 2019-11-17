from django.db import models


# Create your models here.

from usuarios.models import profesor as prof , alumno as alu


class curso(models.Model):

    idCurso = models.CharField(max_length=4)
    title= models.CharField(max_length=20)
    credito = models.IntegerField()

class periodo(models.Model):

    idPeriodo = models.CharField(max_length=4)
    fecha = models.DateTimeField(blank=True,null=True)
    horas = models.IntegerField()
    alumno = models.ForeignKey(alu, on_delete=models.CASCADE)
    estado= models.CharField(max_length=20,blank=True)

class clase(models.Model):

    profesor = models.ForeignKey(prof,on_delete=models.CASCADE)
    alumno = models.ForeignKey(alu,on_delete=models.CASCADE)
