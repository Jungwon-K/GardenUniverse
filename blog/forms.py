from django import forms
from .models import Post, Topic

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'topic']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 15}),
            'topic': forms.CheckboxSelectMultiple(),
        }
        