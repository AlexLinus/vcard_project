from django.shortcuts import render, get_object_or_404, redirect
from .models import Posts, Category, Comments
from .forms import CommentForm
# Create your views here.

def blog_detail(request):
    posts = Posts.objects.filter(is_active=True)[:5]
    return render(request, 'blog/blog.html', context={
        'posts': posts,
    })

def post_detail(request, post_slug):
    post = get_object_or_404(Posts, slug=post_slug, is_active=True)
    if f'post_views_{post.id}' not in request.session:
        request.session[f'post_views_{post.id}'] = post.id
        post.views +=1
        post.save()
        #post.update(views=+1) update не работае с get, только с filter. Поэтому будем мануально сохранять и прибавлять
    categories = Category.objects.filter(is_active=True)
    related_posts = Posts.objects.filter(is_active=True).exclude(id=post.id)[:3]
    comment_form = CommentForm()
    return render(request, 'blog/post_detail.html', context={
        'post': post,
        'categories': categories,
        'related_posts': related_posts,
        'comment_form': comment_form,
    })

def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    return render(request, 'blog/category_detail.html', context={
        'category': category,
    })

def add_comment(request, post_slug):
    post = get_object_or_404(Posts, slug=post_slug)
    full_form = CommentForm(request.POST)
    if full_form.is_valid():
        new_comment = full_form.save(commit=False)
        new_comment.post = post
        new_comment.save()

    return redirect(post)

