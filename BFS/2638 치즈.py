from collections import deque
import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def dfs(x,y):
    arr[x][y]=0
    if not visited[x][y]:
        visited[x][y]=True
        for t in range(4):
            nx=x+dx[t]
            ny=y+dy[t]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and arr[nx][ny]==0:
                dfs(nx,ny)
def check(x,y):
    temp=0
    can=False
    for t in range(4):
        nx=x+dx[t]
        ny=y+dy[t]
        if visited[nx][ny] and arr[nx][ny]==0:
            temp+=1
        if temp==2:
            can=True
            break
    return can
def solution():
    global arr,visited,n,m
    n,m=map(int,input().split())
    arr=[]
    Q=deque([])
    visited=[[False]*m for _ in range(n)]
    for i in range(n):
        arr.append(list(map(int,input().split())))
    dfs(0,0)
    for i in range(n):
        for j in range(m):
            if arr[i][j]==1:
                Q.append([i,j])
    cnt=0
    while Q:
        lq=len(Q)
        temp=[]
        for i in range(lq):
            x,y = Q.popleft()
            if not check(x,y):
                Q.append([x,y])
            else:
                temp.append([x,y])
        for nx,ny in temp:
            dfs(nx,ny)
        cnt+=1
    print(cnt)
    return

if __name__ == '__main__':
    solution()
