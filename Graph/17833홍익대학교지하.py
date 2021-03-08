import sys
from heapq import *
INF=sys.maxsize
input=sys.stdin.readline

def dijkstra(s,v):
    temp=[INF]*(n+1)
    temp[s]=0
    Q=[]
    heappush(Q,(0,s))
    while Q:
        weight,num=heappop(Q)
        if temp[num]!=weight:
            continue
        else:
            for x in adj[num]:
                t=arr[num][x]
                if temp[x]>weight+t:
                    temp[x]=weight+t
                    heappush(Q,(weight+t,x))
    if temp[v]==INF:
        print("-1")
    else:
        print(temp[v])

n=int(input())
s,v=map(int,input().split())
m=int(input())
arr=[[INF]*(n+1) for _ in range(n+1)]
adj=[set() for _ in range(n+1)]
for i in range(m):
    a,b,c,d=map(int,input().split())
    for i in range(n-a+1):
        if arr[c+i][d+i]>b:
            arr[c+i][d+i]=b
            adj[c+i].add(d+i)
        if arr[d+i][c+i]>b:
            arr[d+i][c+i]=b
            adj[d+i].add(c+i)

dijkstra(s,v)
