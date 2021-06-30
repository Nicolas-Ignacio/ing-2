from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Categoria(models.Model):
    idCategoria=models.IntegerField(primary_key=True, verbose_name="id de categoría")
    nombreCategoria = models.CharField(max_length=80,blank=False, verbose_name="nombre de la categoría")

    def __str__(self):
        return self.nombreCategoria


#Create Modelo para productos de la tienda (api)

class Ropa(models.Model):
    idRopa=models.CharField(max_length=15, primary_key=True,verbose_name="Codigo de Producto" )
    marcaRopa=models.CharField(max_length=40, blank=False, null=False , verbose_name="Marca ")
    precioRopa=models.IntegerField(null=False,verbose_name="Precio")
    descripcionRopa=models.CharField(max_length=100,null=False,verbose_name="Descripción")
    imagenRopa=models.ImageField(upload_to="images/", default="sinfoto.jpg", null=False,blank=False,verbose_name="Imagen")
    categoriaRopa=models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __setattr__(self):
        return self.idRopa