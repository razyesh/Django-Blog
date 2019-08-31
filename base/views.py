from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category, Subscribe, Videos
from django.views.generic import ListView, DetailView, CreateView
from .forms import SubscribeForm
from django.contrib import messages


class PostListView(ListView):
    model = Post
    template_name = "homepage/index.html"
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['category_nepal'] = Post.objects.filter(category='1')
        context['category_automobile'] = Post.objects.filter(category='2')
        context['category_mobbiles'] = Post.objects.filter(category='3')
        context['category_computers'] = Post.objects.filter(category='4')
        context['category_gadget_review'] = Post.objects.filter(category='5')
        context['category_jobs'] = Post.objects.filter(category='6')
        context['videos'] = Videos.objects.all()
        return context


class PostListCategories(ListView):
    model = Post
    template_name = "homepage/category.html"
    context_object_name = 'category_posts'
    paginate_by = 5

    def get_queryset(self):
        category_posts = Post.objects.all()
        category_posts = category_posts.filter(
            category__slug=self.kwargs['slug'])
        return category_posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['category_nepal'] = Post.objects.filter(category='1')
        context['category_automobile'] = Post.objects.filter(category='2')
        context['category_mobbiles'] = Post.objects.filter(category='3')
        context['category_computers'] = Post.objects.filter(category='4')
        context['category_gadget_review'] = Post.objects.filter(category='5')
        context['videos'] = Videos.objects.all()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'homepage/post-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['category_nepal'] = Post.objects.filter(category='1')
        context['category_automobile'] = Post.objects.filter(category='2')
        context['category_mobbiles'] = Post.objects.filter(category='3')
        context['category_computers'] = Post.objects.filter(category='4')
        context['category_gadget_review'] = Post.objects.filter(category='5')
        context['videos'] = Videos.objects.all()
        return context


def subscribe(request):
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for Subscribing")
    else:
        form = SubscribeForm()

    return render(request, 'homepage/index.html', {'form': form})


class VideoListView(ListView):
    model = Videos
    template_name = 'homepage/video.html'
    context_object_name = 'videos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
