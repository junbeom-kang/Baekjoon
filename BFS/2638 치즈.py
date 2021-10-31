from collections import deque
import sys
input=sys.stdin.readline
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def solution():
    n,m=map(int,input().spit())
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
        for i in range(len(lq)):
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
