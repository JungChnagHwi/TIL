from django.shortcuts import render
from .models import Article, Comment
# Create your views here.
def index(request):
   
    return render(request, 'articles/index.html')

def create():
    pass

def update():
    pass

def delete():
    pass

def detail():
    pass

def comments():
    pass

def comments_delete():
    pass

def likes():
    pass