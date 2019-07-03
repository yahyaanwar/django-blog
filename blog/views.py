from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify

from . models import Post
from . forms import PostForm
from user . models import CustomUser

def index(request):
    post_list = Post.objects.order_by('create_at').all()
    return render(request, 'blog/index.html', {'post_list':post_list})

def post_detail(request,slug):
    post = Post.objects.get(slug=slug)

    try:
        prev_slug = post.get_previous_by_update_at().slug
    except Post.DoesNotExist:
        prev_slug = False

    try:
        next_slug = post.get_next_by_update_at().slug
    except Post.DoesNotExist:
        next_slug = False

    return render(request, 'blog/post_detail.html',{
        'post':post, 
        'prev_slug': prev_slug, 
        'next_slug': next_slug
    })

@login_required
def create(request):
    post_form = PostForm(request.POST or None)
    if request.method == 'POST':
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('blog:index')
    return render(request, 'blog/create.html',{'form':post_form})