from django.db import models

from user.models import CustomUser

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title