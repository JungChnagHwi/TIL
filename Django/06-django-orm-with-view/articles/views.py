from django.shortcuts import render, redirect #다시 요청
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    # Article.objects.get(id=pk) 이렇게 써도 됨
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)


def new(request):
    return render(request, 'articles/new.html', )

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    #1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    #2 유효성 검사하기 좋아서 많이 쓴단다...
    article = Article(title=title, content=content)
    article.save()

    #3
    # Article.objects.create(title=title, content = content)

    return redirect('articles:index')


def delete(request, pk):
    # 몇 번 게시물 삭제할 것인지 조회
    article = Article.objects.get(pk=pk)
    # 조회한 게시글 삭제
    article.delete()
    return redirect('article:index')

