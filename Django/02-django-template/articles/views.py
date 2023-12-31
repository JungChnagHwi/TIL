from django.shortcuts import render
import random


# Create your views here.
def index(request):
    context = {
        'name': 'Jane',
    }
    return render(request, 'articles/index.html', context)

def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육']
    picked = random.choice(foods)
    empty_list=[]
    context = {
        'foods': foods,
        'picked': picked,
        'empty_list': empty_list
    }
    return render(request, 'articles/dinner.html', context)

def search(request):
    return render(request, 'articles/search.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    #사용자로부터 요청을 받아서
    #요청에서 사용자 입력 데이터를 찾아
    #content에 저장 후 catch 템플릿에 출력
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    # print(request)
    # print(type(request))
    # print(request.META)
    # print(request.GET)
    # print(request.GET.get('message'))
    return render(request, 'articles/catch.html', context)

def greeting(request, name):
    context = {
        'name': name
    }
    return render(request, 'articles/greeting.html', context)

def detail(request, num):
    context = {
        'num': num
    }
    return render(request, 'articles/detail.html', context)

def random_number(request, number):
    next_number = number + 1
    context = {
        'number': number,
        'next_number': next_number
    }
    return render(request, 'articles/random_number.html', context)
    
