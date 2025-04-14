import json
from django.shortcuts import render, get_object_or_404
from .models import Post
from .utils import render_markdown
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

@login_required
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

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'topics']
    template_name = 'blog/post_form.html'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
    

def graph_data(request):
    nodes = []
    links = []

    posts = Post.objects.prefetch_related('topics')

    for post in posts:
        nodes.append({"id": post.title, "group": "post"})
        for topic in post.topics.all():
            nodes.append({"id": topic.name, "group": "topic"})
            links.append({"source": post.title, "target": topic.name})

    unique_nodes = {node['id']: node for node in nodes}.values()

    return JsonResponse({"nodes": list(unique_nodes), "links": links})

def graph_view(request):
    return render(request, 'blog/graph.html')

def home(request):
    return render(request, 'blog/home.html')
