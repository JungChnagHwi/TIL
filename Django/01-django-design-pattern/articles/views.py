from django.shortcuts import render

# Create your views here.
#특정 경로에 대한 처리를 해줄 함수
#매개변수 이름은 내 마음대로 지어도 되는데, 
#framework 쓸 때는 되도록 convention 지키자.
#request 사용자 요청의 모든 정보
def index(request):
    #render 함수의 두 번
    return render(request, 'articles/index.html')