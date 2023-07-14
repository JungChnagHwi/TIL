# GIT 이란?   
> 분산 버전 관리 시스템
- 변화 기록 및 추적
중앙 집중식> 
분산식 > 
gitlab , github 원격저장
### git 영역 
1. working directory : 실제 작업 환경  
ex) 홈펭지를 만들 때,, 로그인 기능을 만들려는데 회원가입 기능이 필요해,, 두 개 파일을 동시에 작없했는데 회원가입 기능을 먼저 완성해야 하니 ver1으로,, 로그인은 ver2로..,,,워킹 디렉토리에서 동시에 작업했더라도 ver1만 staging area로 먼저 옮기는 식
2. staging area : 워킹디렉토리에서 변경된 파일 중 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역 add
3. Repository : 버전 이력과 파일들이 영구적으로 저장되는 여역,, 모든 버전과 변경 이력이 기록됨
- (local 내가 하고 있는 .git) & (remove 분산 시스템에서 회사와 집을 연결하는 원격 저장소)

연습장에서 관리
### git 초기화
```bash
$ git init
```  
- 이 폴더는 (master) 란 이름의 git으로 관리되고 있어

- 버전은 commit (찍기) 이라 불러! 변경된 파일을 저장하는 것
윈도우 - 자격증명관리자 - windows자격 증명 -


### 상태 확인 명령어
```bash
$ git status
```

### staging area 추가
```bash
$ git add {path}<folde_name>/{file_name}
```
### Repository에 저장
```bash
$ git commit -m "commit message"
```
git config --global user.email "jch9937@gmail.com"
git config --global user.name "정창휘"

### git 초기설정
```bash
$ git config --global user.email "jch9937@gmail.com"
$ git config --global user.name "정창휘"
$ git config --global --list  #한 번만
```

### 커밋 기록 확인하기
```bash
$ git log
```
- add 로 변경, commit으로 확정,, 로그로 확인


### 직전 커밋 수정하기
```bash
$ git commit --amend
# vim에서 insest(삽입 상태 만들기) - 내용 수정 - esc(삽입 상태 종료) - :wq(저장 및 종료)
```

### git 설정 초기화
```bash
#vim을 활용해서 설정 제거하기
#vim git 설정 파일 열기
$ vim~/.gitconfig
$ code~/.gitconfig
#insert 키:수정 상태 만들기
#-insert-인 상태에서 모든 내용 삭제
#esc: 수정 상태 종료
#:wq
```

## 원격 저장소 git에 등록
```bash
$ git remote add{remote_nickname}{remote_url}
```
 
## 원격 저장소에 업로드
```bash
$ git push origin master
```
## 원격 저장소에 있는 내용 복제
-최초로 내려받을 때
```bash
$ git clone github url  
```

<<<<<<< HEAD

## !!git push origin master

git clone 주소창


## 원격 저장소 git에 등록
```bash
$ git remote add{remote_nickname}{remote_url}
```
 
## 원격 저장소에 업로드
```bash
$ git push origin master
```
## 원격 저장소에 있는 내용 복제
-최초로 내려받을 때
```bash
$ git clone github url  
```
=======
수정했엉!
>>>>>>> 46460e3e2ea15c62b275a950f310f4d8c5c5f247
