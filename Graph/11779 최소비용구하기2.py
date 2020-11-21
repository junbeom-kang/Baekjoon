import sys
from heapq import *
INF=sys.maxsize
def dijkstra(v):
    ans=[INF]*(n+1)
    ans[v]=0
    heappush(heap,(0,v))
    while heap:
        weight,num=heappop(heap)
        if ans[num]<weight:
            continue
        else:
            for c,d in adj[num]:
                if weight+c<ans[d]:
                    ans[d]=weight+c
                    before[d]=num
                    heappush(heap,(ans[d],d))
    return ans


input=sys.stdin.readline
n=int(input())
m=int(input())
adj=[[]for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    adj[a].append((c,b))
v,e=map(int,input().split())
heap=[]
before=[0]*(n+1)
temp=dijkstra(v)
print(temp[e])
A=[e]
while before[e]!=0:
    A.append(before[e])
    e=before[e]
print(len(A))
print(*A[::-1])