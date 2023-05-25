from django.contrib import admin
from .models import Project

# Desde aqui se impostan todas llos modelos 

#Lista o tupla para definir los campos que solo son de lectura 

#Al registro para la tabla en la base de datos se le tiene que pasar la configuración extendida

#class ProjectAdmin(admin.ModelAdmin):
    #readonly_fields = ('created', 'updated')


admin.site.register(Project)#, ProjectAdmin)