from django.db import models


# Create your models here.

from usuarios.models import profesor as prof , alumno as alu


class curso(models.Model):

    idCurso = models.CharField(max_length=4,unique=True)
    title= models.CharField(max_length=20)
    credito = models.IntegerField()


class seccion(models.Model):

    profesor = models.ForeignKey(prof,on_delete=models.CASCADE)
    curso = models.ForeignKey(curso,on_delete=models.CASCADE)

class clase(models.Model):

    alumno = models.ForeignKey(alu,on_delete=models.CASCADE,default="")
    secc = models.ForeignKey(seccion,on_delete=models.CASCADE,default="")

class periodo(models.Model):

    clas = models.ForeignKey(clase, on_delete=models.CASCADE, default="")
    fecha = models.DateTimeField(auto_now_add=True)
    estado= models.CharField(max_length=20,blank=True)