from django.db import models

# Create your models here.

class Insumos(models.Model):
    nombre = models.CharField(max_length=120,primary_key=True)
    precio = models.IntegerField()
    descripcion = models.TextField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class ImagenGaleria(models.Model):
    imagen = models.ImageField(upload_to='galeria')
    def __img__(self):
        return self.imagen
class ImagenSlider(models.Model):
    imagenSlider=models.ImageField(upload_to='slider')
    def __img__(self):
        return self.imagenSlider
class QuienesSomos(models.Model):
    ident= models.CharField(max_length=40,primary_key=True)
    vision= models.TextField()
    mision= models.TextField()
    
    def __str__(self):
        return self.ident
        