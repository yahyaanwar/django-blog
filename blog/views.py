from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify

from . models import Post
from . forms import PostForm
from user . models import CustomUser

def index(request):
    post_list = Post.objects.order_by('create_at').all()
    return render(request, 'blog/index.html', {'post_list':post_list})

def post_detail(request,slug):
    post = get_object_or_404(Post,slug=slug)

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
            post.user_id = request.user
            post.save()
            return redirect('blog:post_detail', request.POST.get('slug'))
    return render(request, 'blog/create.html',{'form':post_form})

@login_required
def update(request,slug):
    post = get_object_or_404(Post,slug=slug)
    url_referer = (request.META.get('HTTP_REFERER'), reverse('blog:index'))[request.META.get('HTTP_REFERER') == None]
    if request.user == post.user_id:
        post_form = PostForm(request.POST or None, instance= post)
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