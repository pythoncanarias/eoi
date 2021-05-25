from django.db import models

# Create your models here.


class Equipo(models.Model):
    id = models.AutoField(primary_key=True)  # No es estrictamente necesario
    nombre = models.CharField(max_length=100)
    cuartel = models.CharField(max_length=240, blank=True)  # blank=True significa opcional

    def __str__(self):
        return self.nombre


class Poder(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, unique=True)  # No puede haber nombres duplicados

    def __str__(self):
        return self.nombre


class Metahumano(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    identidad = models.CharField(max_length=100)
    nivel = models.PositiveIntegerField(default=1)
    equipo = models.ForeignKey(
        Equipo,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    poderes = models.ManyToManyField(Poder)
    activo = models.BooleanField(default=True)
    foto = models.ImageField(
        blank=True,
        null=True,
        upload_to='metahumans',
    )

    def peligroso(self):
        return self.nivel >= 50

    def __str__(self):
        return f"{self.nombre} [{self.nivel}]"

    def num_poderes(self):
        return self.poderes.count()
