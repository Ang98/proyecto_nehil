"""middlerware para actualizar"""

from django.shortcuts import redirect
from django.urls import reverse

class perfilCompletoMiddleware:

    """perfil"""

    def __init__(self,get_response):
        self.get_reponse = get_response

    def __call__(self, request):
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                perfil = request.user.perfil
                #perfil2= request.user.alumno
                #print(perfil2.profesion)
                if perfil.tipo_usuario=='':
                    if request.path not in [reverse('signup1'),reverse('logout')]:
                        return redirect('signup1')
                else:
                    if perfil.tipo_usuario.upper()=='ALUMNO':
                        alu = request.user.alumno
                        if alu.imagen is None or alu.imagen=='':
                            if request.path not in [reverse('signup2'), reverse('logout')]:
                                return redirect('signup2')
                    if perfil.tipo_usuario.upper() == 'PROFESOR':
                        pro = request.user.profesor
                        if pro.profesion is None :
                            if request.path not in [reverse('signup2'), reverse('logout')]:
                                return redirect('signup2')
        response = self.get_reponse(request)
        return response



