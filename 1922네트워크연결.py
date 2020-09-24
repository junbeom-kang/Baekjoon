import sys
from heapq import *
input=sys.stdin.readline
def find(v):
    if parent[v]==v:
        return v
    else:
        parent[v]=find(parent[v])
        return parent[v]
def merge(a,b):
    global cnt
    q=find(a)
    w=find(b)
    if q==w:
        return
    else:
        cnt+=1
        if q<w:
            parent[w]=q
        else:
            parent[q]=w
        return True

n=int(input())
m=int(input())
parent=[i for i in range(n+1)]
Q=[]
for _ in range(m):
    a,b,c=map(int,input().split())
    heappush(Q,(c,a,b))
cnt=0
ans=0
while cnt!=n-1:
    c,a,b=heappop(Q)
    if merge(a,b):
        ans+=c
print(ans)