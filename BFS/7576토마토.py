from collections import deque
import sys
input=sys.stdin.readline
m,n=map(int,input().split())
dx=[0,0,1,-1]
dy=[-1,1,0,0]
check=[[False for _ in range(m)]for _ in range(n)]
stack=[]
queue=deque()
ans=0
for _ in range(n):
    stack.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if stack[i][j]==1:
            queue.append((i,j))
while queue:
    for _ in range(len(queue)):
        temp=queue.popleft()
        for k in range(4):
            rx=temp[0]+dx[k]
            ry=temp[1]+dy[k]
            if 0<=rx<n and 0<=ry<m:
                if check[rx][ry]==False and stack[rx][ry]==0:
                    stack[rx][ry]=1
                    check[rx][ry]=True
                    queue.append((rx,ry))
    ans+=1
for i in range(n):
    for j in range(m):
        if stack[i][j]==0:
            print(-1)
            sys.exit()
else:
    print(ans-1)

