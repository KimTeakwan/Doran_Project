from django.shortcuts import render

def index(request):
    posts = [
        {
            'username': 'sikboyyy',
            'profile_picture': '/static/main/img/user1.png', # Assuming user will add profile1.jpg
            'image_url': '/static/main/img/aa.jpg', # Assuming user will add post1.jpg
            'likes': 1234,
            'caption': '나 좀 잘생긴 거 같아.'
        },
        {
            'username': 'sikboyyy',
            'profile_picture': '/static/main/img/user1.png', # Assuming user will add profile2.jpg
            'image_url': '/static/main/img/bb.jpg', # Assuming user will add post2.jpg
            'likes': 567,
            'caption': '이건 좀 귀여운듯.'
        }
    ]
    context = {'posts': posts}
    return render(request, 'main/index.html', context)

def search(request):
    return render(request, 'main/search.html')

def messages(request):
    return render(request, 'main/messages.html')

def notifications(request):
    return render(request, 'main/notifications.html')

def create(request):
    return render(request, 'main/create.html')

def profile(request):
    user_profile = {
        'name': 'sikboyyy',
        'username': '@sikboyyy',
        'bio': 'This is my Doran project. I love coding and building awesome things.',
        'banner_url': '/static/main/img/bb.jpg',
        'profile_picture_url': '/static/main/img/user1.png',
        'following': 123,
        'followers': 456,
    }
    posts = [
        {
            'username': 'sikboyyy',
            'profile_picture': '/static/main/img/user1.png',
            'image_url': '/static/main/img/aa.jpg',
            'likes': 1234,
            'caption': '나 좀 잘생긴 거 같아.'
        },
        {
            'username': 'sikboyyy',
            'profile_picture': '/static/main/img/user1.png',
            'image_url': '/static/main/img/bb.jpg',
            'likes': 567,
            'caption': '이건 좀 귀여운듯.'
        }
    ]
    context = {
        'user': user_profile,
        'posts': posts
    }
    return render(request, 'main/profile.html', context)

def login_view(request):
    return render(request, 'main/login.html')

def signup_view(request):
    return render(request, 'main/signup.html')