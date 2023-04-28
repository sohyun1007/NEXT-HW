from django.shortcuts import render, redirect
from .models import Code, Comment
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'home.html')

def create(request):
    if request.method == "POST":
        title = request.POST['title']
        code = request.POST['code']
        content = request.POST['content']

        new_code = Code.objects.create(
            title = title,
            code = code,
            content = content,
            author = request.user,
        )
        return redirect('project')

    return render(request, 'create.html')

def project(request):
    projects = Code.objects.all()
    return render(request, 'project.html', {'projects': projects})

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        exist_user = User.objects.filter(username=username)

        if exist_user:
            user_error = "해당 유저가 이미 존재합니다."
            return render(request, 'signup.html', {'user_error': user_error})

        new_user = User.objects.create_user(
            username = username,
            password = password
        )
        auth.login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('home')

    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user, backend ="django.contrib.auth.backends.ModelBackend")
            return redirect('home')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'home.html')

def detailProject(request, project_id):
    project = Code.objects.get(pk=project_id)
    if request.method == "POST":
        content = request.POST['content']
        Comment.objects.create(
            code = project,
            content = content,
            author = request.user
        )
        return redirect('detailProject', project_id)

    return render(request, 'detail.html', {'project': project})

def deleteProject(request, project_id):
    project = Code.objects.get(pk=project_id)
    project.delete()
    return redirect('project')


def deleteComment(request, project_id, comment_id):
    comment = Comment.objects.filter(pk=comment_id)
    comment.delete()
    return redirect('detailProject', project_id)

@login_required(login_url="/login/")
def edit(request, project_id):
    project = Code.objects.get(pk=project_id)
    return render(request, 'edit.html', {'project': project})