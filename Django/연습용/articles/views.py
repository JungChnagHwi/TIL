from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def hello(request):
    return render(request, 'articles2/hello.html')

def bye(request):
    return render(request, 'articles3/bye.html')