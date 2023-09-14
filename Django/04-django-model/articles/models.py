from django.db import models

# Create your models here.
#테이블 설계도 작성
#테이블에서 id는 장고가 만들어줌
#Model은 model에 관련된 모든 코드가 이미 작성되어 있는 클래스
class Article(models.Model): #models모듈에 Model 클래스를 상속 받고 있어
    title = models.CharField(max_length = 10) #제약조건
    #문자열 넣을 때 사용(최대길이 설정은 필수 인자)
    content = models.TextField()
    #글자수 많을 때 사용
    
    #각 열 이름,,,,,,,,,클래스 title은 charfield의 인스턴스
    #열은 필드,,, 행은 레코드,, 라고 부름
    # charfield, textfield는 데이터 타입
    
    #추가하고 싶으면
    created_at = models.DateTimeField(auto_now_add = True)
    #날짜와 시간 넣을 때 사용,, 
    # auto_now_add -> 데이터가 처음으로 생성될 때 자동으로 현재 날짜시간 저장(작성일)
    updated_at =models.DateTimeField(auto_now=True)
    # auto_now -> 데이터가 저장될 때마다 자동으로 현재 날짜시간 저장(수정일)
    
    ## python manage.py makemigration
    # -> 만약 게시물이 있었다가 추가되면 빈 값으로 추가될 수 없어 불가능
    # 01. default값을 장고가 알아서 넣거나 02. 직접 작성
    # 1번 선택 후 엔터 누르면 기본값 생성
    # 0002_~~ 파일이 생겼는데 0001번 설계도를 의존함, 0001에서 이어가는 개념
    # python manage.py migrate (반영)
    
    
    # Automatic admin interface (관리자 인터페이스)-데이터확인 및 테스트에 용이
    # python manage.py createsuperuser (admin 계정 생성)
    # id, email(선택), password 작성->db에 저장되어 있음
    # 이제 서버 admin 로그인 가능

from django.contrib import admin
from .models import Article

admin.site.register(Article)
#admin.py에 작성한 모델 클래스를 등록해야만 admin site에서 확인 가능

# 데이터베이스 초기화 방법
# migration 파일(0001,0002...), db.sqlite3 파일 2개만 삭제

# 기타
# python manage.py showmigrations (파일들이 migrate 됐는지 여부 확인)
# python manage.py sqlmigrate articles 0001 (해당 파일이 어떻게 번역되어 db에 전달되는지 확인)

    
    
    