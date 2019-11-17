from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError


from usuarios.models import perfil,alumno,profesor
from django.db.utils import IntegrityError

from usuarios.forms import perfilForm,alumnoForm,profesorForm

def login_view(request):

    if request.method == 'POST':

        username = request.POST['user']
        password = request.POST['pass']

        user = authenticate(request, username = username, password= password)
        if user:
            login(request,user)
            return redirect('pagina')
        else:
            return render(request,'users/login1.html',{'error':'usuario no valido'})

    return render (request, 'users/login1.html')

@login_required()
def logout_view(request):

    logout(request)
    return redirect('login')

def signup(request):


    if request.method == 'POST':
        username= request.POST['username']
        pss = request.POST['password']
        pass_con = request.POST['password_confirmation']
        if pss != pass_con:
            return render(request, 'users/signup.html' , {'error':'contraseña de confirmacion diferente'})

        try:
            user = User.objects.create_user(username=username,password=pass_con)

        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'este usuario ya existe'})

        user.save()

        per = perfil(usuario = user)
        per.save()
        return redirect('login')

    return render(request,'users/signup.html')

def signup1(request):

    if request.method == 'POST':
        usuario=request.user
        nombre= request.POST['first_name']
        apellido = request.POST['last_name']
        correo = request.POST['correo']
        tipo= request.POST['select']
        numero = request.POST['numero']
        if tipo == '':

            return render(request, 'users/signup1.html' , {'error': 'seleccione una categoria'})
        else:
            usuario.first_name = nombre
            usuario.last_name = apellido
            usuario.email=correo
            if tipo=='PROFESOR':
                pro = profesor(usuario=usuario)
                pro.save()

            else:
                alu = alumno(usuario=usuario)
                alu.save()

            per = perfil.objects.get(usuario=usuario)
            per.tipo_usuario=tipo
            per.numero= numero
            per.save()

            usuario.save()

            return redirect('signup2')





    return render(request, 'users/signup1.html')

def signup2(request):


    if request.method == 'POST':
        usuario = request.user



        if request.user.perfil.tipo_usuario == 'PROFESOR' or request.user.perfil.tipo_usuario == 'profesor':

            form = profesorForm(request.POST)

            if form.is_valid() :
                tipo = profesor.objects.get(usuario=usuario)
                profe = request.POST['profesion']

                if profe == '':
                    return render(request, 'users/signup2.html', {'error': 'llene todos los datos'})

                tipo.profesion = profe
                tipo.save()
            else:
                form =alumnoForm()



        else:

            form = alumnoForm(request.POST,request.FILES)

            if form.is_valid() :

                data = form.cleaned_data

                tipo = alumno.objects.get(usuario=usuario)
                ima = data['imagen']

                if ima is None:
                    return render(request, 'users/signup2.html', {'error': 'llene todos los datos'})

                tipo.imagen=ima
                tipo.save()
            else:
                form =alumnoForm()


        return redirect('pagina')

    else:
        if request.user.perfil.tipo_usuario == 'PROFESOR' or request.user.perfil.tipo_usuario == 'profesor':
            form = profesorForm()
        else:
            form = alumnoForm()

    return render(request,
                  template_name='users/signup2.html',
                  context={
                      'form':form,
                  })