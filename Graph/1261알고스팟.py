import sys
from heapq import heappush,heappop
dx=[0,0,1,-1]
dy=[1,-1,0,0]
answer=sys.maxsize
def solution(n, m,arr):
    global visited
    dist=[[answer]*m for _ in range(n)]
    heap=[]
    dist[0][0]=0
    heappush(heap,(0,0,0))
    while heap:
        d,x,y=heappop(heap)
        if x==n-1 and y==m-1:
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx and nx<n and 0<=ny and ny<m:
                if arr[nx][ny]==1:
                    if dist[nx][ny]>dist[x][y]+1:
                        dist[nx][ny]=dist[x][y]+1
                        heappush(heap,(dist[nx][ny],nx,ny))
                else:
                    if dist[nx][ny]>dist[x][y]:
                        dist[nx][ny]=dist[x][y]
                        heappush(heap,(dist[nx][ny],nx,ny))

    return dist[n-1][m-1]

n,m=map(int,input().split())
arr=[]
for i in range(m):
    arr.append(list(map(int,input())))

print(solution(m,n,arr))

#print(solution(3,3,[[0,1,1],[1,1,1],[1,1,0]]))