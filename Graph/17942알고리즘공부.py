import sys
from heapq import *
input=sys.stdin.readline

n,m=map(int,input().split())
size=[0]+list(map(int,input().split()))
Q=[]
for i in range(1,n+1):
    heappush(Q,(size[i],i))
arr=[[] for _ in range(n+1)]
check=[False]*(n+1)
cnt=0;
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    arr[a].append((c,b))
ans=0;
while cnt<m:
    a,b=heappop(Q)
    if check[b]:
        continue
    else:
        for q,w in arr[b]:
            size[w]-=q
            heappush(Q,(size[w],w))
        check[b]=True
        cnt+=1
        ans=max(a,ans)
print(ans)

