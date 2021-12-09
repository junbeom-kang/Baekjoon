import sys
from collections import deque
input=sys.stdin.readline
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def solution():
    m,n=map(int,input().split())
    visited=[[[False]*32 for _ in range(m)]for _ in range(n)]
    arr=[[[]for _ in range(m)] for _ in range(n)]
    tt=0
    number=dict()
    for i in range(n):
        temp=input().rstrip()
        for j in range(m):
            arr[i][j]=temp[j]
            if temp[j]=='S':
                start=[i,j,0]
                visited[i][j][0]=True
            elif temp[j]=='E':
                end=(i,j)
            elif temp[j]=='X':
                number[(i,j)]=tt
                tt+=1
    Q=deque([start])
    cnt=0
    can=True
    while Q and can:
        lq=len(Q)
        for i in range(lq):
            x,y,w=Q.popleft()
            if x==end[0] and y==end[1] and w==(1<<tt)-1:
                can=False
                break
            else:
                for t in range(4):
                    nx=x+dx[t]
                    ny=y+dy[t]
                    nw=w
                    if 0<=nx<n and 0<=ny<m and arr[nx][ny]!='#' and not visited[nx][ny][nw]:
                        visited[nx][ny][nw]=True
                        if arr[nx][ny]=='X':
                            itemNumber=number[(nx,ny)]
                            if not w&(1<<itemNumber):
                                nw+=(1<<itemNumber)
                            visited[nx][ny][nw]=True
                        Q.append([nx,ny,nw])
        cnt+=1
    print(cnt-1)

    return

if __name__ == '__main__':
    solution()

