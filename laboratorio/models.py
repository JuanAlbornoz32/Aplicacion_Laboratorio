from django.db import models
#Se importa datetime para obtener la fecha actual en el default de la fecha de fabricacion del producto
import datetime

# Create your models here.

annos_choices = []

for r in range(2015, (datetime.datetime.now().year+1)):
    annos_choices.append((r, r))

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=250, verbose_name="Nombre Laboratorio")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    def __str__(self):
        return self.nombre
    
class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=250, verbose_name="Nombre Director")
    laboratorio = models.OneToOneField("Laboratorio", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=250, verbose_name="Nombre Producto")
    laboratorio = models.ForeignKey("Laboratorio", on_delete=models.CASCADE)
    f_fabricacion = models.DateField(validators=[], default=datetime.date.today, verbose_name="Fecha de Fabricacion")
    p_costo = models.DecimalField(decimal_places=2, max_digits=12, verbose_name="Precio Costo")
    p_venta = models.DecimalField(decimal_places=2, max_digits=12, verbose_name="Precio Venta")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    def __str__(self):
        return self.nombre