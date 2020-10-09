import sys
from heapq import *
input=sys.stdin.readline


def dijkstra(k):
    ans[k]=0
    heappush(heap,[0,k])
    while heap:
        weight,num=heappop(heap)
        if weight>ans[num]:
            continue
        else:
            for c,b in adj[num]:
                if weight+c<ans[b]:
                    ans[b]=weight+c
                    heappush(heap,[ans[b],b])
def dijkstra1(s):
    ans=[INF]*n
    ans[s]=0
    Q=[]
    heappush(Q,(0,s))
    while Q:
        a,b=heappop(Q)
        if ans[b]>a:
            continue
        else:
            for q,w in adj[b]:
                if ans[w]>ans[b]+q:
                    ans[w]=ans[b]+q
                    heappush(Q,(ans[w],w))
    return ans

v,e=map(int,input().split())
k=int(input())
INF=sys.maxsize
adj=[[]for _ in range(v+1)]
ans=[INF]*(v+1)
heap=[]
for _ in range(e):
    a,b,c=map(int,input().split())
    adj[a].append([c,b])

dijkstra1(k)
for i in ans[1:]:
    if i==INF:
        print('INF')
    else:
        print(i)