# GIT 이란?   
> 분산 버전 관리 시스템
- 변화 기록 및 추적
중앙 집중식> 
분산식 > 
gitlab , github 원격저장
### git 영역 
- working directory : 실제 작업 환경  
ex) 홈펭지를 만들 때,, 로그인 기능을 만들려는데 회원가입 기능이 필요해,, 두 개 파일을 동시에 작없했는데 회원가입 기능을 먼저 완성해야 하니 ver1으로,, 로그인은 ver2로..,,,워킹 디렉토리에서 동시에 작업했더라도 ver1만 staging area로 먼저 옮기는 식
- staging area : 워킹디렉토리에서 변경된 파일 중 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역
- Repository : 버전 이력과 파일들이 영구적으로 저장되는 여역,, 모든 버전과 변경 이력이 기록됨

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
$ git config --global --list
```
쉬프트 인서트
