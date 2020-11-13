import sys
from heapq import *
input=sys.stdin.readline
INF=sys.maxsize
n,e=map(int,input().split())
adj=[[]for _ in range(n+1)]
for _ in range(e):
    a,b,c=map(int,input().split())
    adj[a].append((c,b))
    adj[b].append((c,a))
one,two=map(int,input().split())

def dijkstra(a,b):
    Q=[]
    ans=[INF]*(n+1)
    ans[a]=0
    heappush(Q,(0,a))
    while Q:
        weight,num=heappop(Q)
        if weight>ans[num]:
            continue
        else:
            for c,d in adj[num]:
                if weight+c<ans[d]:
                    ans[d]=weight+c
                    heappush(Q,(ans[d],d))
    if ans[b]==INF:
        print(-1)
        sys.exit()
    return ans[b]


print(min(djekstra(1,one)+djekstra(one,two)+djekstra(two,n),djekstra(1,two)+djekstra(two,one)+djekstra(one,n)))
