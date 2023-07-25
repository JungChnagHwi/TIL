<<<<<<< HEAD
# # import requests

# # url = 'https://random-data-api.com/api/v2/users'
# # response = requests.get(url).json()
# # print(response)

# list_of_book = ['장화홍련전','가락국 신화','온달 설화','금오신화','이생규장전','만복자서포기','수성지','백호집','원생몽유록','홍길동전','장생전','도문대작','옥루몽','옥련몽']

# rental_book = ['장생전','원생몽유록','이생규장전','장화홍련전','수성지','백호집','난중일기','홍길동전','만복자서포기']

# for i in rental_book:
#     if i in list_of_book:
#        continue
#     print('모든 도서가 대여 가능한 상태입니다.')
#     if i not in list_of_book:
#         print(f'{i} 은/는 보유하고 있지 않습니다.')



# list_of_book = ['장화홍련전','가락국 신화','온달 설화','금오신화','이생규장전','만복자서포기','수성지','백호집','원생몽유록','홍길동전','장생전','도문대작','옥루몽','옥련몽']
# rental_book = ['장생전','위대한 개츠비', '원생몽유록','이생규장전', '데미안', '장화홍련전','수성지','백호집','난중일기','홍길동전','만복자서포기']

# missing_book = list(i for i in rental_book if i not in list_of_book)

# for i in rental_book:
#     if i not in list_of_book:
#         print(f'{i} 을/를 보충하여야 합니다.')
# if missing_book==[]:
#     print('모든 도서가 대여 가능한 상태입니다.')
     
import sys

n = int(sys.stdin.readline())

for _ in range(n):

    left = []
    right = []

    pwd = list(sys.stdin.readline().rstrip())

    for char in pwd:

        if char == ">":
            if right:
                left.append(right.pop())

        elif char=="<":
            if left:
                right.append(left.pop())

        elif char=="-":
            if left:
                left.pop()

        else:
            left.append(char)

    print("".join(left) + "".join(reversed(right)))
=======
# #1
# # main.py

# # 아래 함수를 수정하시오.
# def count_character(str1, str2):
#     count=0
#     for char in str1:
#         if str2 == char:
#             count+=1
#     return count
    
# result = count_character("Hello, World!", "o")
# print(result) # 2

#2
# main.py

# 아래 함수를 수정하시오.
def find_min_max(list):
    ans=(min(list), max(list))    
    return ans

result = find_min_max([3, 1, 7, 2, 5])
print(result) # (1, 7)



>>>>>>> e45505bed3ca2340e8dda99fcdddecaabe55d1d4

