from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.index, name="post_list"),
    path("slug/", views.post_detail, name="post_detail"),
]
