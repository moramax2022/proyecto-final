from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from educa.models import Post
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from educa.forms import UsuarioForm
from educa.models import Avatar, Post, Mensaje
from django.contrib.auth.admin import User
 
 
def index(request):
   posts = Post.objects.order_by('-publicado_el').all()
   return render(request, "educa/index.html", {"posts": posts})
 
class PostDetalle(DetailView):
   model = Post
 
class PostListar(ListView):
   model = Post 
 
class PostCrear(LoginRequiredMixin, CreateView):
   model = Post
   success_url = reverse_lazy("educa-listar")
   fields = '__all__'
 
class PostBorrar(LoginRequiredMixin, DeleteView):
   model = Post
   success_url = reverse_lazy("educa-listar")
 
class PostActualizar(LoginRequiredMixin, UpdateView):
   model = Post
   success_url = reverse_lazy("educa-listar")
   fields = "__all__"
 
class UserSignUp(CreateView):
   form_class = UsuarioForm
   template_name = 'registration/signup.html'
   success_url = reverse_lazy('educa-listar')
 
#http://localhost:8000/educa/login/?next=/educa/listar/
class UserLogin(LoginView):
   next_page = reverse_lazy('educa-listar')
 
class UserLogout(LogoutView):
   next_page = reverse_lazy('educa-listar')
 
class AvatarActualizar(UpdateView):
   model = Avatar
   fields = ['imagen']
   success_url = reverse_lazy('educa-listar')
 
 
class UserActualizar(UpdateView):
   model = User
   fields = ['first_name', 'last_name', 'email']
   success_url = reverse_lazy('educa-listar')
 
 
class MensajeDetalle(LoginRequiredMixin, DetailView):
   model = Mensaje
 
class MensajeListar(LoginRequiredMixin, ListView):
   model = Mensaje 
 
class MensajeCrear(CreateView):
   model = Mensaje
   success_url = reverse_lazy("educa-mensajes-crear")
   fields = ['nombre', 'email', 'texto']
 
class MensajeBorrar(LoginRequiredMixin, DeleteView):
   model = Mensaje
   success_url = reverse_lazy("educa-mensajes-listar")

