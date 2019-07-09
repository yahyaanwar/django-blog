import re
from django.db import models

from user.models import CustomUser

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True)
    thumb = models.ImageField(blank=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def trContent(self):
        return re.sub('\s*(<[^>]+>)\s*', ' ', self.content)[:150]