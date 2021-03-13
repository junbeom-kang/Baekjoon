import sys
from heapq import *
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
R=10**6
INF=sys.maxsize

def dijkstra():
    temp=[INF]*n
    temp[0]=0
    Q=[]
    heappush(Q,(0,0))
    while Q:
        weight,where=heappop(Q)
        if temp[where]!=weight:
            continue
        else:
            for w,c in adj[where]:
                if temp[w]>weight+c:
                    temp[w]=weight+c
                    heappush(Q,(temp[w],w))
    return temp[m]


n,m=map(int,input().split())
color=[]
arr=[]
adj=[[] for _ in range(n)]
for i in range(n):
    color.append(int(input()))
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    for j in range(i+1,n):
        if arr[i][j]!=0:
            if color[i]!=color[j]:
                adj[i].append((j,R+arr[i][j]))
                adj[j].append((i,R+arr[i][j]))
            else:
                adj[i].append((j,arr[i][j]))
                adj[j].append((i,arr[i][j]))
ans=dijkstra()
print(ans//R,ans%R)