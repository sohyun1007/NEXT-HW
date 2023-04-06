from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def create(request):
    if request.method == "POST":
        new_todo = Todo.objects.create(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('home')
    return render(request, 'create.html')

def home(request):
    Todos = Todo.objects.all()
    return render(request, 'home.html', {'Todos': Todos})


def detail(request, detail_id):
    Todos = Todo.objects.filter(id=detail_id)
    return render(request, 'detail.html', {'Todos': Todos})

def update(request, detail_id):
    if request.method == "POST":
        Todo.objects.filter(id=detail_id).update(
            title = request.POST['title'],
            content = request.POST['content'],
        )
        return redirect('home')
    Todos = Todo.objects.get(id=detail_id)
    return render(request, 'update.html', {'Todos': Todos})

def delete(request, detail_id):
    Todos = Todo.objects.filter(id=detail_id)
    Todos.delete()
    return redirect('home')
