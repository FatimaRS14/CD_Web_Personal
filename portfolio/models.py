from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects") #esto es para tener mejor organización dentro de los archivos que se suben para que todo este dentro de un directorio especifico
    link = models.URLField(verbose_name="Dirección Web", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
   

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['-created']#esto sirve para ir ordenando los post de manera ascendente   
   
    def __str__(self):
        return f'{self.title}'

