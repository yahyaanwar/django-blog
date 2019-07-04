from django.shortcuts import render

from . models import Post

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