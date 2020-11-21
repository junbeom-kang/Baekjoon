import sys
from heapq import *
def dijkstra(a):
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
    return ans
input=sys.stdin.readline
INF=sys.maxsize
N=int(input())
for _ in range(N):
    n,m,t=map(int,input().split())
    adj=[[]for _ in range(n+1)]
    s,g,h=map(int,input().split())
    stack=[]
    for _ in range(m):
        a,b,d=map(int,input().split())
        adj[a].append((d,b))
        adj[b].append((d,a))
    temp=dijkstra(s)
    temp2=dijkstra(h)
    temp3=dijkstra(g)
    for _ in range(t):
        q=int(input())
        if temp[g]+temp2[g]+temp2[q]==temp[q] or temp[h]+temp2[g]+temp3[q]==temp[q]:
            stack.append(q)
    stack.sort()
    for i in stack:
        print(i,end=' ')