from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


#CustomUsermodel 로 대체하기
#별도의 User 클래스 정의 없이 내장된 User 클래스를 사용했음
#간편하지만 개발자가 직접 수정할 수 없는 문제가 존재
#User 클래스도 AbstractUser 를 상속받기 때문에 커스텀 USser도 기존 User와 완전히 같은 모습
# setting 에 ' AUTH_USER_MODEL = 'accounts.User' ' 
# 기본 USER 인 auth.User에서 우리가 작성한 USER 모델로 변경
## admin.py에 등록 
# 프로젝트 중간에 AUTH_USER_MODEL 을 변경할 수 없음 
#이미 진행중이면 데이터베이스 초기화(sqlite 삭제, 데이터 파일 0001 00002 삭제)