import sys
from heapq import *
INF=sys.maxsize
input=sys.stdin.readline
v,e=map(int,input().split())
k=int(input())
adj=[[]for _ in range(v+1)]
heap=[]
ans=[INF]*(v+1)
ans[k]=0
for _ in range(e):
    a,b,c=map(int,input().split())
    adj[a].append((c,b))
heappush(heap,(0,k))
while heap:
    weight,num=heappop(heap)
    if weight>ans[num]:
        continue
    else:
        ans[num]=weight
        for c,b in adj[num]:
            if weight+c<ans[b]:
                ans[b]=weight+c
                heappush(heap,(ans[b],b))
for i in ans[1:]:
    if i==INF:
        print('INF')
    else:
        print(i)

