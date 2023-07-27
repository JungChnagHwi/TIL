# 관통 Project

## 7/21
### 오늘 목표-api key 불러와서 활용해보기!
- 데이터 크롤링
- 브라우저에 url 작성 및 파이썬requests 를 통해 클라이런트가 서버에 요청,
- api, 클라이언트가 원하는 기능을 수행하기 위해서 서버 측이 만들어 놓은 프로그램 ex) 데이터 저장,조회,수정,삭제// 서버 측에 특정 주소로 요청이 오면 정해진 기능을 수행함,, 정보를 가지고 있는 해당 서버를 찾아야 함
- open api, 주의사항,, 너무 많은 계정에서 동시에 요청하면 서버 마비,, 그래서 API KEY를 활용해 사용자를 확인, 사용량 제한 걸어두고 초과하면 요금 청구
- json이란? 경량의 텍스트 기반의 데이터 형식, 파이썬(dictionay)랑 비슷하
({키:값, 키:값,...}),, 키는 문자열/값은 다양한 데이터 유형
- 파싱: 데이터를 의미 있는 구조로 분석(원하는 형태로 변환)하고 해석하는 과정
- json.loads(): json 형식을 dict형태로 변환