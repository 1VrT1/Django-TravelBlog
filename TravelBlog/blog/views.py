import random

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.base import View
from .forms import PostsForm
from .models import Posts, Category


class GetCategory:

    def get_category(self):
        return Category.objects.all()


class WelcomeView(View):
    """Приветственная страница"""
    def get(self, request):
        return render(request, 'blog/welcome.html')


class BlogPublicView(GetCategory, ListView):
    """Страница с постами всех пользователей"""
    queryset = Posts.objects.filter(is_public=True)
    paginate_by = 2


class BlogHomeView(GetCategory, ListView):
    """Страница с постами авторизованного пользователя"""
    model = Posts
    template_name_suffix = '_homelist'
    paginate_by = 2

    def get_queryset(self):
        return Posts.objects.filter(blogger=self.request.user)


class FilterPublicView(GetCategory, ListView):
    """Фильтр по категориям для страницы с постами всех пользователей"""
    model = Posts
    paginate_by = 1

    def get_queryset(self):
        return Posts.objects.filter(is_public=True, category__url=self.kwargs['category_url'])


class FilterHomeView(GetCategory, ListView):
    """Фильтр по категориям для страницы с постами авторизованного пользователя"""
    model = Posts
    template_name_suffix = '_homelist'
    paginate_by = 1

    def get_queryset(self):
        return Posts.objects.filter(blogger=self.request.user, category__url=self.kwargs['category_url'])


class BlogDetailView(DetailView):
    """Основное описание поста"""
    model = Posts
    slug_field = 'url'


class CreatePostView(CreateView):
    """Создание поста"""
    model = Posts
    form_class = PostsForm

    def form_valid(self, form):
        form.instance.blogger = self.request.user
        form.instance.url = self.request.user.username + str(random.randrange(100000, 999999))
        form.save()
        return redirect('home')

    def success_url(self):
        return redirect('home')


class UpdatePostView(UpdateView):
    """Редактирование поста"""
    model = Posts
    form_class = PostsForm
    slug_field = 'url'


class DeletePostView(DeleteView):
    """Удаление поста"""
    model = Posts
    slug_field = 'url'
    success_url = reverse_lazy('home')


# def create_post(request):
#     if request.method == 'POST':
#         form = PostsForm(request.POST)
#         if form.is_valid():
#             Posts.objects.create(**form.cleaned_data, blogger=request.user)
#             return redirect('home')
#     else:
#         form = PostsForm()
#         return render(request, 'blog/posts_form.html', context={'form': form})
