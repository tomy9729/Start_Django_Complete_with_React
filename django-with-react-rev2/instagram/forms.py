from django import forms
from django.db.models import fields
from .models import Post

class PostForm(forms.ModelForm) : 
    class Meta : 
        model = Post
        fields = ["photo", "caption", "location"]
        widgets = {
            "caption" : forms.Textarea,
        }