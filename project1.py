import sys
input=sys.stdin.readline

n = int(input())
box=[]
for i in range(n):
  k = int(input())
  box.append(k)

stack = []
result = []
num = 1
for x in box:
    while num <= x:
        stack.append(num)
        result.append('+')
        num += 1
    if stack[-1] == x:
        stack.pop()
        result.append('-')
    else:
        result = 'NO'

result = '\n'.join(result)
print(result)

