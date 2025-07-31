from django.shortcuts import redirect
from django.shortcuts import render 
from django.utils import timezone
from .models import Post
from .forms import PostForm


def post_detail(request, pk):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {})
def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

if request.method == "POST":
    [...]
else:
    form = PostForm()

if form.is_valid():
    post = form.save(commit=False)
    post.author = request.user
    post.published_date = timezone.now()
    post.save()