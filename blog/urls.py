from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:page>/", views.index, name="pagination"),
    path("create/", views.create, name="create"),
    path("<slug:slug>/update/", views.update, name="update"),
    path("<slug:slug>/delete/", views.delete, name="delete"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    
    
   
]
