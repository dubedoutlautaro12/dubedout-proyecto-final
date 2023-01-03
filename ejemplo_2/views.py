from django.shortcuts import render
from django.views.generic import CreateView, ListView
from ejemplo_2.models import Post
from django.urls import reverse_lazy

def index(request):
    return render(request, 'ejemplo_2/index.html', {})


class PostList(ListView):   
    model = Post

class PostCrear(CreateView):
    model = Post
    success_url= reverse_lazy('ejemplo-dos-listar')
    fields= '__all__'


