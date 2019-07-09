from django.forms import ModelForm
from django_summernote.widgets import SummernoteInplaceWidget

from .models import Post

# Create the form class.
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'thumb']
        widgets = {
            'content': SummernoteInplaceWidget(),
        }