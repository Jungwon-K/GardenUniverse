from django.shortcuts import render, get_object_or_404
from .models import Post
from .utils import render_markdown
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.content = render_markdown(post.content)

    return render(request, 'blog/post_detail.html', {'post': post})

def post_list(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})
