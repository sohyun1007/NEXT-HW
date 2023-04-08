from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def home(request):
    Todos = Todo.objects.all()
    return render(request, 'home.html', {'Todos': Todos})

def create(request):
    if request.method == "POST":
        new_Todo = Todo.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            end_date = request.POST['end_date']
        )
        return redirect('home')
    return render(request, 'create.html')

def detail(request, detail_pk):
    Todos = Todo.objects.filter(pk=detail_pk)
    return render(request, 'detail.html', {'Todos': Todos})

def update(request, detail_pk):
    Todos = Todo.objects.filter(pk=detail_pk)
    if request.method == "POST":
        Todo.objects.filter(pk=detail_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            end_date = request.POST['end_date']
        )
        return redirect('home')
    return render(request, 'update.html', {'Todos': Todos})   

def delete(request, detail_pk):
    Todos = Todo.objects.filter(pk=detail_pk)
    Todos.delete()
    return redirect('home')