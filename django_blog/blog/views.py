from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.db import connection
from django.http import HttpResponse


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    # Set model to Post view to query
    model = Post
    template_name = 'blog/home.html'

    # looking for object list so set to name above
    context_object_name = 'posts'

    # Order by recent with minus sign
    ordering = ['-date_posted']

    # adds pagination and number to show each page
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    # get user
    def get_queryset(self):
        # get username from url
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        # return user posts ordered by most recent
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    # Set model to Post view to query
    model = Post


class PostCreateView(PermissionRequiredMixin, CreateView):

    permission_required = 'can_create_post'
    # Set model to Post view to query
    model = Post

    # Fields we want in the form
    fields = ['title', 'content']

    # override form valid method to get current user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(PermissionRequiredMixin, UpdateView):

    permission_required = 'can_update_post'
    # Set model to Post view to query
    model = Post

    # Fields we want in the form
    fields = ['title', 'content']

    # override form valid method to get current user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # check correct user can update post
    def test_func(self):
        post = self.get_object()
        if self.request.user.is_superuser:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # Set model to Post view to query
    model = Post
    success_url = '/'

    # check correct user can update post
    def test_func(self):
        post = self.get_object()
        if self.request.user.is_superuser:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
