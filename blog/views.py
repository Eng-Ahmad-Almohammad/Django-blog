from xml.etree.ElementTree import Comment
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Post, Category
from .forms import CommentForm
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


def category(request, slug):
    category = get_object_or_404(Category, slug = slug)
    posts = category.posts.filter(status = Post.ACTIVE)
    return render(request, 'blog/category.html', {'posts': posts, 'category': category})

def search(request):
    query = request.GET.get('query', '')
    posts = Post.objects.filter(status = Post.ACTIVE).filter(Q(title__icontains = query) | Q(intro__icontains = query) | Q(body__icontains = query))

    return render(request, 'blog/search.html', {'posts': posts, 'query': query})