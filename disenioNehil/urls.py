from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static


from disenioNehil import views as local
from posts import views as views_post

from usuarios import views as users_view
from pagina import views as pagina_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('angel/',local.hola_mundo,name='hora'),
    path('posts/',views_post.list_p),
    path('users/login', users_view.login_view , name = 'login'),
    path('users/logout', users_view.logout_view , name = 'logout'),

    path('users/signup', users_view.signup, name='signup'),
    path('users/signup1', users_view.signup1, name='signup1'),
    path('users/signup2', users_view.signup2, name='signup2'),

    path('pagina/', pagina_view.principal, name='pagina'),
    path('pagina/alumno', pagina_view.principal, name='alumno'),
    path('pagina/profesor/<int:id>', pagina_view.profe, name='profe'),
    path('pagina/profesor/tomarAsistencia/<int:id>', pagina_view.profe, name='asistencia'),
    path('pagina/profesor/curso', pagina_view.cursoReq, name='curso'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
