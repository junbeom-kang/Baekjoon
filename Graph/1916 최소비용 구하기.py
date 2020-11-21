import sys
from heapq import *
INF=sys.maxsize
input=sys.stdin.readline
def dijkstra(s,e):
    ans=[INF]*(n+1)
    ans[s]=0
    Q=[]
    heappush(Q,(0,s))
    while Q:
        cost,b=heappop(Q)
        if ans[b]<cost:
            continue
        for q,w in adj[b]:
            if cost+q<ans[w]:
                ans[w]=cost+q
                heappush(Q,(ans[w],w))
    return ans[e]

n=int(input())
m=int(input())
adj=[[]for _ in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    adj[a].append((c,b))
s,e=map(int,input().split())
print(dijkstra(s,e))




