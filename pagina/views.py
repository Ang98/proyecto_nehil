from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from usuarios.models import profesor
from pagina.models import seccion,curso,clase,periodo
# Create your views here.
@login_required()
def principal(request):

    if  request.user.perfil.tipo_usuario.upper()=='PROFESOR':

        return redirect('curso')

    return render(request,'pagina/principal.html')


def cursoReq(request):
    cur = list(seccion.objects.filter(profesor=request.user.profesor))

    if  request.method=='POST':

        nu= request.POST['select']
        cu=curso.objects.get(pk=nu)
        aux= seccion.objects.get(profesor=request.user.profesor,curso=cu)
        numero=aux.pk
        return redirect('profe',id=numero)

    return render(request
                  ,'pagina/proIni.html'
                  ,context={
                    'cursos': cur,

        }
                  )

def profe(request,id):
    sec = seccion.objects.get(pk=id)


    return render(request,
                  'pagina/profesor.html',
                  context={
                  'curso':sec.curso,
                  'profe':request.user,
                  'numero':id,
    })



def asistencia(request,id):
    sec = seccion.objects.get(pk=id)
    alumnos=list(clase.objects.filter(secc=sec))


    return render(request,
                  'pagina/tomarAsis.html',
                  context={
                      'alumnos':alumnos,
                      'numero': id,
                  }
                  )

def cursoAlu(request):

    cur= list(clase.objects.filter(alumno=request.user.alumno))




    return render(request,
                  'pagina/cursosAlu.html',
                  context={
                      'cursos': cur,
                      }
                  )