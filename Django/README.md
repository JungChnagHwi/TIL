# Django

1. 가상환경 생성(gitignore 생성 후)
- $ python -m venv 이름
2. 가상환경 활성화(on/off) 두 개의 가상환경 키고 싶으면 두 개의 gitbash에 따로 켜야 함
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

//

## 프로젝트 관리
- TIL, 학습하고 있는 각종 폴더, 관통 PJT
- git으로 관리중
  - TIL/**/*.py
  - git으로 관리 되지 않아야 할 목록
    - .gitignore : 가상환경 생성(git으로 관리 X)

## 가상환경
- Python 애플리케이션과 그에 따른 패키지들을 격리하여 관리할 수 있는 독립적인 실행 환경
- git으로 관리 안한다. -> .gitignore
- requirement.txt 해당 프로젝트를 위한 독립 환경 목록 구성
- local작업할 때, 가상환경 안만들고, global에 django 설치하고 작업 진행하면, 매번 똑같은 환경에서 진행하는데 왜 필요할까? 

## 가상환경 생성
```bash
#작업 위치 잘 확인하자
#파이썬아 / -m 모듈써서 /  virtual enviroment 모듈써서 / venv라는 폴더에 가상환경 만들어줘
$ python -m venv {folder_name}
```

## 가상환경 실행
```bash
$ ls
{ venv folder_name}/
$ source { foledr_name }/Scripts/Activate
( folder_name )
$ pip list
```

## Django 설치
```bash
$ pip install django
```

### 다른 작업 환경을 위한 설정
```bash
#현재 pip목록을 얼린다.
$ pip freeze > requirements.txt

#requirements.txt 파일에 적힌 내용으로 설치
$ pip install -r requirements.txt
```

## 장고 프로젝트 생성
```bash
$ django-admin startproject {프로젝트 이름}
$ cd offline

# 현재 작업 위치에 프로젝트 생성 
django-admin startproject {프로젝트 이름} .
```
## 장고 서버 실행
```bash
$ python manage.py runserver
```

## 앱 생성 및 등록
```bash
$ python manage.py startapp 이름(articles) (복수형 권장)
# articles을 프로젝트 - settings.py - installed apps에 등록
```

## articles app의 메인 페이지 화면에 띄우기
1. 클라이언트가 요청 보낼 경로 지정하기
2. 특정 경로에 요청이 왔을 때, 그 요청에 적절한 처리하기 -> views.py
3. 적절한 처리 과정에서 template(html) 이 필요하다면, 작성하기 -> templates/*.html
4. 작성된 template을 사용자에게 반환하기 -> views에 정의한 함수의 return 값