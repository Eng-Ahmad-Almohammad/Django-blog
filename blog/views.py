from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Category
from .forms import CommentForm, PostForm
# Create your views here.

class PostListView(ListView):
    template_name = 'core/frontpage.html'
    # model = Post
    queryset = Post.objects.filter(status = Post.ACTIVE)
    context_object_name = 'posts'

class PostDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        context = {}
        slug = kwargs.get('slug', '')
        post = get_object_or_404(Post, slug=slug, status = Post.ACTIVE)
        form = CommentForm()
        context['post'] = post
        context['form'] = form
        return render(request, 'blog/post_detail.html',context)

    def post(self, request, *args, **kwargs):
        slug = kwargs.get('slug', '')
        post = get_object_or_404(Post, slug=slug)
        category_slug = kwargs.get('category_slug', '')
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail',category_slug = category_slug, slug = slug)

        form = CommentForm()
        return render(request, 'blog/post_detail.html', {'form':form})

class PostCreateView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request, *args, **kwargs):
        form = PostForm()
        return render(request, 'blog/create_post.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('post_detail', post.category.slug, post.slug)
        
        return render(request, 'blog/create_post.html', {'form':form})

class UserPosts(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'blog/my_posts.html'
    # queryset = Post.objects.filter(author = user)
    # context_object_name = 'posts'

    # def get_context_data(self,**kwargs):
    #     context = super(UserPosts,self).get_context_data(**kwargs)
    #     context['blabla'] = 'Hello World'
    #     return context

def category(request, slug):
    category = get_object_or_404(Category, slug = slug)
    posts = category.posts.filter(status = Post.ACTIVE)
    return render(request, 'blog/category.html', {'posts': posts, 'category': category})

def search(request):
    query = request.GET.get('query', '')
    posts = Post.objects.filter(status = Post.ACTIVE).filter(Q(title__icontains = query) | Q(intro__icontains = query) | Q(body__icontains = query))

    return render(request, 'blog/search.html', {'posts': posts, 'query': query})