# CLI
- Command line interface

- 새 폴더 만들기
```bash
$ mkdir new_folder
```

- 작업 위치를 new_folder로 이동
```bash
$ cd new_folder #cd .. 상위 위치로 이동
```

- 현재 작업 위치를 열기
```bash
# . => 현재 위치(상대경로)
$ start .
# . => 현재 위치를 vs코드로 열기
$ code .
```

- 현재 작업 위치의 파일 목록
```bash
$ ls

```

- 파일의 이름을 바꾸거나 위치를 옮기거나
```bash
$ mv {이동할 대상}{이동될 위치}  #위치는 디렉토리
$ mv {이름 바꿀 대상}{바꿀 이름}
```

### 상대 경로 / 절대 경로
1. 절대 경로     
SAFY@DESKTOP-MDJG1NJ MINGW64 ~/new_folder
https:// ~~~

2. 상대 경로
- 나를 기준으로 경로를 지정
여기부터 조퇴

- 삭제
```bash
$ rm{파일명}
$ rm -r {폴더}
```
ex) python(명령대상) /-v(명령), -:약어, --원본
CLI 에선 명령대상 생략

api : 제공해주는 공개 정보, 응용 프로그램, 
오류 의미 4--: 클라이언트 잘못,, 5--: 서버 잘못
성공 시 2--