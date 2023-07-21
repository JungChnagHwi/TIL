#서버에 데이터 달라 요청하는 법
# import requests
# url = 'https://fakestoreapi.com/carts'
# response = requests.get(url)

# print(response.json())

#날씨 데이터 수집
import json
json_data = '''
{
    "name": "싸피",
    "age": 53,
    "hobby": [
        "공부",
        "축구"
    ]
}
'''
data = json.loads(json_data)
#print(data)

#json에서 원하는 데이터만 가져오기
name = data.get('name')
#print(name)

lnt = 37.56
lon = 126.97

