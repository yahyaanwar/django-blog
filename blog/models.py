from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title

