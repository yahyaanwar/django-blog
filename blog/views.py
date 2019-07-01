from django.shortcuts import render

from . models import Post

def index(request):
    post_list = Post.objects.order_by('create_at').all()
    return render(request, 'blog/index.html', {'post_list':post_list})

def post_detail(request,slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/post_detail.html',{'post':post})