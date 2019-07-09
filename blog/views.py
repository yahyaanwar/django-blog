from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from . models import Post
from . forms import PostForm
from user . models import CustomUser

def index(request,page=1):
    post_list = Post.objects.order_by('-create_at').all()
    
    paginator = Paginator(post_list, 5)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:

        posts = paginator.page(paginator.num_pages)
    content = {
        'post_list':posts,
        'pg_range':{
            'left': posts.number-3,
            'right':posts.number+3
        },
    }
    return render(request, 'blog/index.html', content)
    

def post_detail(request,slug):
    post = get_object_or_404(Post,slug=slug)

    try:
        prev_post = post.get_previous_by_create_at()
        prev_data = {
            'title': prev_post.title,
            'slug': prev_post.slug
        }
    except Post.DoesNotExist:
        prev_data = False

    try:
        next_post = post.get_next_by_create_at()
        next_data = {
            'title': next_post.title,
            'slug': next_post.slug
        }
    except Post.DoesNotExist:
        next_data = False

    return render(request, 'blog/post_detail.html',{
        'post':post, 
        'prev': prev_data, 
        'next': next_data
    })

@login_required
def create(request):
    post_form = PostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user_id = request.user
            post.save()
            return redirect('blog:post_detail', request.POST.get('slug'))
    return render(request, 'blog/create.html',{'form':post_form})

@login_required
def update(request,slug):
    post = get_object_or_404(Post,slug=slug)
    url_referer = (request.META.get('HTTP_REFERER'), reverse('blog:index'))[request.META.get('HTTP_REFERER') == None]
    if request.user == post.user_id:
        post_form = PostForm(request.POST or None, request.FILES or None, instance=post)
        if request.method == 'POST':
            if post_form.is_valid():
                post_form.save()
                return redirect('blog:post_detail', request.POST.get('slug'))
        content = {
            'form':post_form,
            'post':post,
            'back':url_referer
        }
    else:
        return redirect('blog:post_detail', slug)
    return render(request, 'blog/update.html',content)

@login_required
def delete(request,slug):
    post = get_object_or_404(Post,slug=slug)
    if request.user == post.user_id:
        post.delete()
    else:
        return redirect('blog:post_detail', slug)
    return redirect('blog:index')