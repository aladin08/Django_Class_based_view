from re import template
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
class PostList(ListView):
    model = Post        # in template we can use either [object_list, post_list]
    ## Attributes
    context_object_name = 'all_posts' # second option
    ordering = ['created_date']
    ## To get only the active posts
    #queryset = Post.objects.filter(active=True)
    #template_name = 'post/test.html'


    def get_queryset(self):
        return Post.objects.filter(active=True)

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['myname'] = 'boutabia alaeddine'
        context['lastname'] = 'python developer'
        return context


class PostDetail(DetailView):
    model = Post


class PostCreate(CreateView):
    model = Post

class PostDelete(DeleteView):
    model = Post


class PostUpdate(UpdateView):
    model = Post