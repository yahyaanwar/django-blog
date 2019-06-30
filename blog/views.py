from django.shortcuts import render

def index(request):
    return render(request, 'blog/index.html')

def post_detail(request):
    return render(request, 'blog/post_detail.html')