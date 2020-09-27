import sys
from heapq import *
input=sys.stdin.readline

n,m=map(int,input().split())
adj=[[]for _ in range(n+1)]
degree=[0]*(n+1)
Q=[]
for _ in range(m):
    a,b=map(int,input().split())
    degree[b]+=1
    adj[a].append(b)

for i in range(1,n+1):
    if degree[i]==0:
        heappush(Q,i)
ans=[]
for i in range(n):
    temp=heappop(Q)
    ans.append(temp)
    for j in adj[temp]:
        degree[j]-=1
        if degree[j]==0:
            heappush(Q,j)
print(*ans)
