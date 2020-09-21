import sys
input=sys.stdin.readline
from collections import deque
def solution(n,m,adj):
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    big=0
    time=0
    for i in range(n):
        for j in range(m):
            if adj[i][j]==1:
                size=0
                Q=deque([(i,j)])
                while Q:
                    temp=Q.popleft()
                    if adj[temp[0]][temp[1]]==1:
                        adj[temp[0]][temp[1]]=-1
                        size+=1
                        for w in range(4):
                            nx=temp[1]+dx[w]
                            ny=temp[0]+dy[w]
                            if 0<=nx<m and 0<=ny<n and adj[ny][nx]==1:
                                Q.append([ny,nx])
                time+=1
                big=max(size,big)
    return time,big
n,m=map(int,input().split())
adj=[list(map(int,input().split()))for _ in range(n)]
a,b=solution(n,m,adj)
print(a)
print(b)