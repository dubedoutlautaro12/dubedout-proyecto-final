from django.shortcuts import render
from django.views.generic import CreateView, ListView, CreateView, DeleteView, UpdateView, DetailView
from ejemplo_2.models import Post
from django.urls import reverse_lazy
from ejemplo_2.forms import UsuarioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from ejemplo_2.models import Avatar, Post, Mensaje
from django.contrib.auth.admin import User


@login_required
def index(request):
    posts = Post.objects.order_by('-publicado_el').all()
    return render(request, 'ejemplo_2/index.html', {'posts': posts})


class PostList(ListView):   
    model = Post

class PostCrear(LoginRequiredMixin, CreateView):
    model = Post
    success_url= reverse_lazy('ejemplo-dos-index')
    fields= '__all__'


class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url= reverse_lazy('ejemplo-dos-index')

class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url= reverse_lazy('ejemplo-dos-index')
    fields = '__all__'


class PostDetalle(DetailView):
    model = Post

class UserSignUp(CreateView):
    form_class= UsuarioForm
    template_name= 'registration/signup.html'
    success_url= reverse_lazy('ejemplo-dos-index')

class UserLogin(LoginView):
    next_page= reverse_lazy('ejemplo-dos-index')

class UserLogout(LogoutView):
    next_page= reverse_lazy('ejemplo-dos-index')
    

class AvatarActualizar(UpdateView):
    model= Avatar
    fields= ['imagen']
    success_url= reverse_lazy('ejemplo-dos-index')


class UserActualizar(UpdateView):
    model = User
    fields = ['first_name','last_name','email']
    success_url= reverse_lazy('ejemplo-dos-index')


class MensajeDetalle(LoginRequiredMixin, DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje  

class MensajeCrear(CreateView):
    model = Mensaje
    success_url = reverse_lazy('ejemplo-dos-index')
    fields = ['nombre', 'email', 'texto']

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("listar-mensajes")