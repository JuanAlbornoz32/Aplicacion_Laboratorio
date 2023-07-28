from django.db import models
#Se importa datetime para obtener la fecha actual en el default de la fecha de fabricacion del producto
import datetime

# Create your models here.

annos_choices = []

for r in range(2015, (datetime.datetime.now().year+1)):
    annos_choices.append((r, r))

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=250, verbose_name="Nombre Laboratorio")
    ciudad = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ciudad")
    pais = models.CharField(max_length=100, blank=True, null=True, verbose_name="Pais")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    num_visitas = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre
    
class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=250, verbose_name="Nombre Director")
    laboratorio = models.OneToOneField("Laboratorio", on_delete=models.CASCADE, verbose_name="Laboratorio")
    especialidad = models.CharField(max_length=100, blank=True, null=True, verbose_name="Especialidad")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=250, verbose_name="Nombre Producto")
    laboratorio = models.ForeignKey("Laboratorio", on_delete=models.CASCADE, verbose_name="Laboratorio")
    f_fabricacion = models.IntegerField(choices=annos_choices, verbose_name="Fecha de Fabricacion")
    p_costo = models.DecimalField(decimal_places=2, max_digits=12, verbose_name="Precio Costo")
    p_venta = models.DecimalField(decimal_places=2, max_digits=12, verbose_name="Precio Venta")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    def __str__(self):
        return self.nombre