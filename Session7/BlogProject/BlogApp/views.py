from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def home(request):
    articles = Article.objects.all()
    categorys = ['daily', 'fashion', 'study']
    count = articles.count()
    return render(request, "home.html", {'articles': articles, 'categorys': categorys, 'count': count})

def create(request):
    categorys = ['daily', 'fashion', 'study']
    if request.method == "POST":
        new_article = Article.objects.create(
            title = request.POST['title'],
            category = request.POST['category'],
            content = request.POST['content'],
        )
        return redirect('home')
    return render(request, "create.html", {'categorys': categorys})

def detail(request, category_nm):
    all_count = Article.objects.all().count()
    articles = Article.objects.filter(category=category_nm)
    count = articles.count()
    categorys = ['daily', 'fashion', 'study']
    return render(request, "detail.html", {'articles': articles, 'categorys': categorys, 'count': count, 'all_count': all_count})