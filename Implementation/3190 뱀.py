import sys
from collections import deque


def get(state):
    if state == 1:
        return 0, 1
    elif state == 2:
        return 1, 0
    elif state == 3:
        return 0, -1
    else:
        return -1, 0


def change(now, d):
    if now == 1:
        if d == 'L':
            return 4
        else:
            return 2
    elif now == 2:
        if d == 'L':
            return 1
        else:
            return 3
    elif now == 3:
        if d == 'L':
            return 2
        else:
            return 4
    else:
        if d == 'L':
            return 3
        else:
            return 1

input=sys.stdin.readline
n=int(input())
arr=[[0]*(n+2) for _ in range(n+2)]
arr[0]=[-1]*(n+2)
arr[n+1]=[-1]*(n+2)
for i in range(1,n+1):
    arr[i][0]=-1
    arr[i][n+1]=-1
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    arr[a][b]=1
t=int(input())
way=deque()
for i in range(t):
    a,b=input().split()
    way.append((a,b))
day=0
arr[1][1]=-1
snake=deque([[1,1]])
state=1
x=1
y=1
while True:

    if way:
        if way[0][0]==str(day):
            _,s=way.popleft()
            state=change(state,s)
    nx,ny=get(state)
    x=x+nx;y=y+ny
    day+=1
    if arr[x][y]==-1:
        print(day)
        break
    if arr[x][y]==0:
        snake.append([x,y])
        q,w=snake.popleft()
        arr[x][y]=-1
        arr[q][w]=0
    else:
        snake.append([x,y])
        arr[x][y]=-1
    #print(x, y, day, state)
