# Django

1. 가상환경 생성
- $ python -m venv 이름
2. 가상환경 활성화(on/off) 두 개의 가상환경 키고 싶으면 두 개의 gitbash를 켜야 함
- $ source venv/Scripts/activate /// deactivate 로 off
3. django 설치
- $ pip install Django
4. 의존성 파일 생성
- pip freeze > requirements.txt 
- (팀프로젝트 때 어떤 패키지 어떤 버전으로 깔려 있는 지 공유하기 위해)
5. gitignore 파일 생성(첫add전),, git저장소 생성
6. Django 프로젝트 생성
- $ django-admin startproject firstpjt .
7. django 서버실행
- python manage.py runserver // 컨트롤+c(서버 종료)

//

app - 독립적으로 작동하는 기능 단위 모듈
생성 - 등록
- $ python manage.py startapp 이름(articles) 생성( 앱 이름 복수형을 권장)
- articles을 프로젝트 - settings.py - installed apps 에 등록
- 
//

MVC == MTV <-> V == T and C == V 

project구조
-settings.py - 모든 설정 관리
-url.py  - url과 적절한 views(contraller)를 연결

app구조
-admin.py 관리자용 페이지 설정
-model.py 데이터 관련된 model 처리 M
-views.py http 요철을 처리하고 해당 요청에 대한 응답을 반환 V

//

요청과 응답

