from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {'posts': posts}
    return render(request, 'main/index.html', context)

def search(request):
    return render(request, 'main/search.html')

def messages(request):
    return render(request, 'main/messages.html')

def notifications(request):
    return render(request, 'main/notifications.html')

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    
    context = {'form': form}
    return render(request, 'main/create.html', context)

def profile(request):
    return render(request, 'main/profile.html')

def login_view(request):
    return render(request, 'main/login.html')

def signup_view(request):
    return render(request, 'main/signup.html')
