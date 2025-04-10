from django.shortcuts import render, get_object_or_404
from .models import Post
from .utils import render_markdown
from django.shortcuts import render
from .models import Post

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.content = render_markdown(post.content)

    return render(request, 'blog/post_detail.html', {'post': post})

def post_list(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})
