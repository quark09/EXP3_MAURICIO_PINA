from django.db import models

# Create your models here.
class Categoria(models.Model):
    codigo_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre



class Producto(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    

    def __str__(self):
        return self.nombre