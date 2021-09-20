from django.conf import settings
from django.db import models
from django.utils import timezone

#Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    @property
    def get_courses(self):
        return self.curso_set.all()

class Curso(models.Model):
    nombre = models.CharField(max_length=10)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    turno = models.CharField(max_length=15)
    año_cursada = models.IntegerField()

    def __str__(self):
        return self.nombre

    @property
    def get_notes(self):
        return self.nota_set.all()
    
class Nota(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)
    texto = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id)


