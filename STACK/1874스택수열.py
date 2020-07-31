from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
number=deque()
stack=deque()
ans=[]
NO=False
for i in range(1,n+1):
    number.append(i)
for i in range(n):
    a=int(input())
    while number and number[0]<=a: #in 을 쓰는건 시간복잡도 O(n)
        stack.append(number.popleft())
        ans.append('+')
    if stack[-1]!=a:
        NO=True
    else:
        stack.pop()
        ans.append('-')
if NO:
    print('NO')
else:
    for i in ans:
        print(i)