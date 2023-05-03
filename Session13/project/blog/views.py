from django.shortcuts import render, redirect
from django.contrib import auth
from .models import User, Post, Comment

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        exist_user = User.objects.filter(username=username)
        
        if exist_user:
            user_error = "해당 유저가 이미 존재합니다."
            return render(request, 'blog/signup.html', {'user_error': user_error})

        new_user = User.objects.create_user(
            username = username,
            password = password
        )

        auth.login(request, new_user)
        return redirect('blog:home')
    return render(request, 'blog/signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('blog:home')
    return render(request, 'blog/login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'blog/home.html')

def create(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        new_post = Post.objects.create(
            title = title,
            content = content,
            author = request.user
        )
        return redirect('blog:home')
    return render(request, 'blog/create.html')

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == "POST":
        comment = request.POST['comment']
        new_comment = Comment.objects.create(
            content = comment,
            post = post,
            author = request.user
        )
        return redirect('blog:detail', post_pk)
    return render(request, 'blog/detail.html', {'post':post})

def update(request, post_pk):
    return render(request, 'blog/update.html')

def delete(request, post_pk):
    return redirect('blog:home')

def deleteComment(request, post_pk, comment_pk):
    comment = Comment.objects.filter(pk=comment_pk)
    comment.delete()
    return redirect('blog:detail', post_pk)

def all(request, user_pk):
    posts = Post.objects.all()
    return render(request, 'blog/all.html', {'posts': posts})