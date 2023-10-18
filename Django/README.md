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

## Migrations
-model클래스의 변경사항(생성,수정,삭제)등 을 DB에 최종 반영하는 방법
-model class ->makemigrations->migration파일(0001_initial.py)->migrate-> dbsql
-   python manage.py makemigrations(작성) ,
-   python manage.py migrate(DB에 전달)

## ORM
- Object Relational Mapping
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 기술
-
- QuerySet API 실습 사전 준비
- 장고가 QuerySet API 로 요청하면 ORM을 거쳐 sql에 보내고 QuerySet(다중) or instance(하나)를 받아옴
- Article.objects.all() == Model class.Manager.Queryset API
- pip install ipython(터미널에서 색깔 입히는 기능),,, 
- pip install django-extensions(확장 프로그램 기능),, 
- 설치하고 'django_extensions' app목록에 추가, requirements에도 추가
- Django shell 실행 -> 'pyhton manage.py shell_plus'(확장 프로그램),,, QuerySet API가 django 프로젝트에 영향을 끼치기 때문에,, 근데 shell이 뭐냐?,,, 나가는 법->exit()
- shell_plus 환경에서 데이터 crud,,, (tip, ctrl + l 터미널 창 정리????)



## 데이터 객체를 만드는 3가지 방법
- shell_plus 환경
### 1번
- article = Article(),, Article(class) 로부터 article(instance) 생성
- article.title = 'first',, 인스턴스 변수(title)에 할당
- article.content = 'first',, 인스턴스 변수(content)에 할당
- Article.objects.all()(all은 전체 조회),, QuerySet [] 확인
- article.save(),, 저장해야 함
- article.id,, aricle.pk(장고는 pk 지원, pk=id),, article.title, article.content... 확인
- Query Set도 index 존재,, Article.objects.all()[0] 이렇게 조회 가능
- Article.objects.filter(content__contains='dja'),,,특정 레코드에 대한 조건 조회
- 기타 등등 기능 장고 공식 문서 참고

### 2번
- article = Article(title = 'second', content='django!')
- 1번 반복(저장 - 확인)

### 3번
- Article.objects.create(title='third', content='django!')
- 1번 반복(저장 - 확인)
- 유효성 검사를 하기 힘들어 잘 안씀?

### CRUD
- Article.objects.get(pk=1),, 단일 데이터 조회(둘 이상은 오류)
- Article.objects.filter(content='django!'),, 특정 조건 데이터 조회
- articles = Article.objects.all()
- for article in articles: print(article.title) 이런식으로 사용 가능
- 
- 데이터 수정,,
- article = Article.objects.get(pk=1) 수정할 인스턴스 조회
- article.title = 'byebye' 변경
- article.save() 저장 및 article.title 확인
- 만약 데이터 수정 시 제약조건을 벗어났다면 기입은 되는데 나중에 유효성 검사 해야 함?? 담 시간에.
- 
- 데이터 삭제,,
- article = Article.objects.get(pk=1) 삭제할 인스턴스 조회
- article.delete() 삭제,, 더 이상 조회 안됨

sou



## 09.auth
- http, 비연결지향, 서버는 요청에 대한 응답을 보낸 후 연결을 끊음,
무상태, 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
- 상태가 없다는 것은 , 로그인상태를 유지할 수 없고 장바구니 상태를 유지할 수 없음
- 이때 쿠키를 사용, 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
- 클라이언트 측에서 저장되는 작은 데이터 파일이며, 사용자 인증,추적 상태 유지 등에 사용되는 데이터 저장 방식
- 쿠키 키벨류 형태로 저장, 이렇게 쿠키를 저장해놨다가 동일한 서버에 재요청시 쿠키를 함께 전송, 
- 사용 목적, 세션관리(로그인, 아이디 자동완성, 공지 하루 안보기, 팝업 체크, 장바구니), 개인화(사용자 선호, 테마 등의 설정), 트래킹(사용자 행동 기록 및 분석)
-세션이란? 서버 측에서 생성되어 클라이언트와 서버 간의 상태를 유지, 상태 정보를 저장하는 데이터 저장방식,, 쿠키에 세션 데이터를 저장하여 매 요청 시마다 세션 데이터를 함께 보냄


## 10. REST framework
- API , 애플리케이션과 프로그래밍으로 소통하는 방법, 클라이언트-서버처럼 서로 다른 프로그램에서 요청과 응답을 받을 수 있도록 만든 체계
- REST(Representationnal State Transfer) : API 서버를 개발하기 위한 일종의 소프트웨어 설계 방식 , 약속(규칙X)
- RESTful API: '자원을 정의' 하고 '자원에 대한 주소를 지정' 하는 전반적인 방법을 서술
- 자원을 정의하고 주소를 지정하는 방법 : 
1. 자원의 식별
-URI(Uniform Resource Identifier) 통합 자원 식별자 : 인터넷에서 리소스(자원)를 식별하는 문자열 ex)URL(Uniform Resource Locater) 통합 자원 위치 : 네트워크 상에 리소스가 어디 있는지를 알려주기 위한 약속
-> http://www.example.com:80/path/to/myfile.html?key1=value1&key2=value2#SomewhereinTheDocument
(Schema)://,,Domain Name,, 80port,, path to the file,, ?parameters,, #Anchor
2. 자원의 행위
-HTTP Methods - GET, POST, PUT, DELETE
-
3. 자원의 표현
-JSON
-궁극적으로 표현되는 데이터 결과물
- 장고에서 템플릿 역할을 프론트엔드 프레임워크가 대체하여 JSON 파일을 넘겨줌

- DRF
- Serialization 직렬화
- 여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정