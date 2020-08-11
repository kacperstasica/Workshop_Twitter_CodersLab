from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    TemplateView,
)

from .forms import PostForm
from .models import Post


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-creation_date']
    paginate_by = 5


class AddPostView(LoginRequiredMixin, CreateView):
    template_name = 'posts/add_post.html'
    form_class = PostForm
    success_url = reverse_lazy(
        'posts:post-list'
    )


    def get_initial(self):
        self.initial['user'] = self.request.user
        return super().get_initial()