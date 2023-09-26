
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # 요청의 메서드가 POST라면 (create)
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # 유효성 검사 진행
        # 유효성 검사가 통과된 경우
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    # 요청의 메서드가 POST가 아니라면 (new)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')




def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 요청의 메서드가 POST라면 (update)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid:
            form.save()
            return redirect('articles:detail', article.pk)
    # 요청의 메서드가 POST가 아니라면 (edit)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)









# HW참고
# from django.views.decorators.http import require_http_methods, require_POST,require_safe
# from django.shortcuts import get_object_or_404


# @require_POST()
# def delete(request,pk):
#     chatting = get_object_or_404(Chat,pk=pk)
#     chatting.delete()
#     return redirect("chattings:index")

# @require_safe()
# def detail(request,pk):
#     chatting = get_object_or_404(Chat,pk=pk)
#     context = {
#         'chatting':chatting,
#     }
#     return render(request,'chattings/detail.html',context)

# @require_http_methods(["GET", "POST"])
# def create(request):
#     if request.method == 'POST':
#         form = ChatForm(request.POST,request.FILES)
#         if form.is_valid:
#             chatting = form.save()
#             return redirect('chattings:detail',chatting.pk)
#     else:
#         form = ChatForm()
#     context={
#         'form':form
#     }
#     return render(request,'chattings/create.html',context)