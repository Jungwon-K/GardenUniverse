from django import forms
from .models import Post, Topic

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'topics']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 15}),
            'topics': forms.CheckboxSelectMultiple(),
        }
        