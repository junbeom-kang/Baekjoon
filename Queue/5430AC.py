import sys
from collections import deque
input=sys.stdin.readline
T=int(input())
data=[]
stack=[]
for i in range(T):
    check=True
    data=input().rstrip()
    n=int(input())
    que=list(input().rstrip()[1:-1].split(','))
    if n==0:
        que.pop()
    que=deque(que)
    where=-1
    for i in data:
        if i=='R':
            where*=-1
        elif i=='D':
            if not que:
                check=False
            elif where==1:
                if que:
                    que.pop()
            elif where==-1:
                if que:
                    que.popleft()
    if check:
        if where==-1:
            print('[',end='')
            for i in range(len(que)):
                if i==len(que)-1:
                    print(que[i],end='')
                else:
                    print(que[i],end=',')
            print(']')
        else:
            print('[',end='')
            for i in range(len(que)-1,-1,-1):
                if i==0:
                    print(que[i],end='')
                else:
                    print(que[i],end=',')
            print(']')
    else:
        print('error')

