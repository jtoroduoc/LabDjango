from django.db import models

# Create your models here.
class Auto(models.Model):
    transmision_choices = [
        ('AT', 'Automatica'),
        ('MT', 'Mecanica')
    ]
    ppu = models.CharField(max_length=6, 
                          verbose_name="Patente",
                          primary_key=True,
                          unique=True,
                          blank=False,
                          null=False)
    marca = models.CharField(max_length=10, verbose_name="Marca")
    modelo = models.CharField(max_length=10, verbose_name="Modelo")
    año = models.IntegerField(verbose_name="Año")
    transmision = models.CharField(max_length=2, choices=transmision_choices)

    def __str__(self):
        return self.ppu + " : " + self.marca
    