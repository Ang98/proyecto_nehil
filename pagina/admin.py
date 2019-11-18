from django.contrib import admin
from pagina.models import curso,periodo,clase,seccion
# Register your models here.


@admin.register(curso)
class cursoAdmin(admin.ModelAdmin):
    list_display = ('idCurso','title','credito')
    list_display_links = ('idCurso','title')

@admin.register(periodo)
class periodoAdmin(admin.ModelAdmin):
    list_display = ('pk','clas','estado')
    list_display_links = ('pk','clas','estado')

@admin.register(clase)
class claseAdmin(admin.ModelAdmin):
    list_display = ('pk','secc','alumno')
    list_display_links = ('pk','secc','alumno')

@admin.register(seccion)
class seccionAdmin(admin.ModelAdmin):
    list_display = ('pk','profesor','curso')
    list_display_links = ('pk','profesor','curso')