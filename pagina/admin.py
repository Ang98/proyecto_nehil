from django.contrib import admin
from pagina.models import curso,periodo,clase
# Register your models here.


@admin.register(curso)
class cursoAdmin(admin.ModelAdmin):
    list_display = ('idCurso','title','credito')
    list_display_links = ('idCurso','title')

@admin.register(periodo)
class periodoAdmin(admin.ModelAdmin):
    list_display = ('pk','alumno','estado')
    list_display_links = ('pk','alumno','estado')

@admin.register(clase)
class claseAdmin(admin.ModelAdmin):
    list_display = ('pk','profesor','alumno')
    list_display_links = ('pk','profesor','alumno')