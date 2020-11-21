from collections import deque
import sys
input=sys.stdin.readline
que=deque([])
n=int(input())
for i in range(n):
    a=input().split()
    if a[0]=='push':
        que.append(a[1])
    elif a[0][0]=='f':
        if que:
            print(que[0])
        else:
            print('-1')
    elif a[0][0]=='b':
        if que:
            print(que[-1])
        else:
            print('-1')
    elif a[0][0]=='s':
        print(len(que))
    elif a[0][0]=='e':
        if que:
            print(0)
        else:
            print(1)
    else:
        if que:
            print(que.popleft())
        else:
            print('-1')
