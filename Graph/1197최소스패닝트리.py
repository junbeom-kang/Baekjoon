import sys
from heapq import *
def find(v):
    if parent[v]==v:
        return v
    else:
        parent[v]=find(parent[v])
        return parent[v]

def merge(q,w):
    if q<w:
        parent[w]=q
    else:
        parent[q]=w


input=sys.stdin.readline
v,e=map(int,input().split())
heap=[]
ans=0
parent=[i for i in range(v+1)]
for _ in range(e):
    a,b,c=map(int,input().split())
    heappush(heap,(c,a,b))
while v!=1:
    c,a,b=heappop(heap)
    q=find(a)
    w=find(b)
    if q!=w:
        merge(q,w)
        v-=1
        ans+=c
print(ans)