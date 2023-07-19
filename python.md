## 파이썬 기초
- 2진수 0b  bin()
- 8진수 0o  oct()
- 16진수 0x  hex()
- 0.1 은 근삿값,, 1.2-1.1=0.09999999987/3.2-3.1=0.1000000000009
- import math, math.isclose(a,b) a와b는 같은 걸로 보자 ,, is가 붙으면 True&False 형식 약속
- sequence type - str,list,tuple,range
- slicing 특정 부분의 값을 추출,, [1:2] 이런거,, slicing 출력은 범위 넘어도 출력 가능,, A[1:3:a] a만큼 건너뛰어 출력
- \n 줄바꿈, \t 탭, \\ 백슬래시, \' 작은따옴표, \" 큰따옴표
- f-스트링 = '{}{}{}'.format(a,b,c) = '%s %d %s' % (a, b, c)
- 집합의 계산: | 합집합, - 차집합, & 교집합
- 암시적 형변환 : 3+5.0=8,,, True+3=4,, True+False=1, 0이 아닌 수는 True
- 비교연산자 : 2.0 is 2 = False 래퍼런스(주소)를 비교해서

## 파이썬 함수
- 내장 함수 import 없이 사용 가능 ex) print는 출력,, return은 반환값 + 종료
- 매개변수:함수를 정의할 때 함수가 받을 값을 나타내는 변수
- 인자:함수를 호출할 때, 실제로 전달되는 값, 반드시 입력&전달
- def a(x,y): 어쩌구, a(특정값, 특정값) -> x,y는 매개, 특정값이 인자
- 기본값 할당 def a(x, y=30): 이러면 a(특정값) 이러면 y=30으로 출력
- a(y=특, x=특) 되고 a(y=특, '특') 은 안됨
- def a(*x):  *붙이면 튜플로 들어감, 매개변수 몇 개인지 모를 때
- **x 이면 정해지지 않은 키워드 인자 ,, dictionay 형태로 {x:특, y:특} 나옴
- 위치/ 기본/ 가변 / 키워드 / 가변 키워드 - 인자 권장순서
- scope 공간&번위,,,내부는 local, 외부는 global
- local - Enclosed - global - built in , local이 마지막 ppt예시 확인!!
- iterable:반복가능한 객체
- zip(*iterables) : 같은 인덱스를 튜플로 묶어서 출력
- lambda 이름 없은 함수, m=list(map(lambda x: x*2, m)) 이렇게 쓰면 좋아
-