# import requests

# url = 'https://random-data-api.com/api/v2/users'
# response = requests.get(url).json()
# print(response)

list_of_book = ['장화홍련전','가락국 신화','온달 설화','금오신화','이생규장전','만복자서포기','수성지','백호집','원생몽유록','홍길동전','장생전','도문대작','옥루몽','옥련몽']

rental_book = ['장생전','원생몽유록','이생규장전','장화홍련전','수성지','백호집','난중일기','홍길동전','만복자서포기']

for i in rental_book:
    if i in list_of_book:
       continue
    print('모든 도서가 대여 가능한 상태입니다.')
    if i not in list_of_book:
        print(f'{i} 은/는 보유하고 있지 않습니다.')



list_of_book = ['장화홍련전','가락국 신화','온달 설화','금오신화','이생규장전','만복자서포기','수성지','백호집','원생몽유록','홍길동전','장생전','도문대작','옥루몽','옥련몽']
rental_book = ['장생전','위대한 개츠비', '원생몽유록','이생규장전', '데미안', '장화홍련전','수성지','백호집','난중일기','홍길동전','만복자서포기']

missing_book = list(i for i in rental_book if i not in list_of_book)

for i in rental_book:
    if i not in list_of_book:
        print(f'{i} 을/를 보충하여야 합니다.')
if missing_book==[]:
    print('모든 도서가 대여 가능한 상태입니다.')
     


