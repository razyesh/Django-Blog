from django.shortcuts import render, redirect
from .models import Post, Category, Subscribe
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
        context['categories']= Category.objects.all()
        context['category_nepal'] = Post.objects.filter(category='1')
        context['category_automobile'] = Post.objects.filter(category='2')
        context['category_mobbiles'] = Post.objects.filter(category='3')
        context['category_computers'] = Post.objects.filter(category='4')
        context['category_gadget_review'] = Post.objects.filter(category='5')
        context['category_jobs'] = Post.objects.filter(category='6')
        return context 

class PostListCategories(ListView):
    model = Post
    template_name = "homepage/index.html"
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        posts = Post.objects.all()
        posts = posts.filter(category = self.kwargs['id'])
        return posts
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories']= Category.objects.all()
        context['category_nepal'] = Post.objects.filter(category='1')
        context['category_automobile'] = Post.objects.filter(category='2')
        context['category_mobbiles'] = Post.objects.filter(category='3')
        context['category_computers'] = Post.objects.filter(category='4')
        context['category_gadget_review'] = Post.objects.filter(category='5')
        return context 

class PostDetail(DetailView):
    model = Post
    template_name = 'homepage/post-detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories']= Category.objects.all()
        context['category_nepal'] = Post.objects.filter(category='1')
        context['category_automobile'] = Post.objects.filter(category='2')
        context['category_mobbiles'] = Post.objects.filter(category='3')
        context['category_computers'] = Post.objects.filter(category='4')
        context['category_gadget_review'] = Post.objects.filter(category='5')
        return context 

def subscribe(request):
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Thanks for Subscribing")
            return redirect('/%20subscribe')
    else:
        form = SubscribeForm()
    
    return render(request, 'homepage/subscribe.html', {'form':form})

