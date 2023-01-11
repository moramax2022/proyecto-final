"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from ejemplo.views import (AltaAlumno, AltaDocente, BorrarFamiliar, BuscarDocente, index, mostrar_familiares, BuscarFamiliar, AltaFamiliar, ActualizarFamiliar, mostrar_alumnos , BuscarAlumno)
from educa.views import (PostCrear, PostListar, PostDetalle, PostActualizar, index, UserSignUp, UserLogin, UserLogout, PostBorrar, AvatarActualizar, UserActualizar, MensajeCrear, MensajeDetalle, MensajeListar)
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns =[ 
    
      path('admin/', admin.site.urls),
      path('saludar/', index),
      path('mi-familia/', mostrar_familiares),
      path('mi-familia/buscar', BuscarFamiliar.as_view()),
      path('mi-familia/alta', AltaFamiliar.as_view()),
      path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
      path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()), 
      path('success_updated_message/',TemplateView.as_view(template_name="ejemplo/success_updated.html")),
      path('Alumnos/', mostrar_alumnos ), 
      path('Alumnos/buscar', BuscarAlumno.as_view()),
      path('Alumnos/alta', AltaAlumno.as_view()),
      path('Docentes/alta', AltaDocente.as_view()),
      path('Docentes/buscar', BuscarDocente.as_view()),
      path('success_updated_message/',TemplateView.as_view(template_name="ejemplo/success_updated_message.html")),
      path('educa/', index, name="educa-index"),
      path('educa/<int:pk>/detalle/', PostDetalle.as_view(), name="educa-detalle"),
      path('educa/listar/', PostListar.as_view(), name="educa-listar"),
      path('educa/crear/', (PostCrear.as_view()), name="educa-crear"),
      path('educa/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="educa-borrar"),
      path('educa/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="educa-actualizar"),
      path('educa/signup/', UserSignUp.as_view(), name ="educa-signup"),
      path('educa/login/', UserLogin.as_view(), name= "educa-login"),
      path('educa/logout/', UserLogout.as_view(), name="educa-logout"),
      path('educa/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="educa-avatars-actualizar"),
      path('educa/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="educa-users-actualizar"),
      path('educa/mensajes/crear/', MensajeCrear.as_view(), name="educa-mensajes-crear"),
      path('educa/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="educa-mensajes-detalle"),
      path('educa/mensajes/listar/', MensajeListar.as_view(), name="educa-mensajes-listar"),
  ]
  
 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
