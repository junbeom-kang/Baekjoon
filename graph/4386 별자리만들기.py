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
n=int(input())
parent=[i for i in range(n)]
where=[]
heap=[]
ans=0
for _ in range(n):
    x,y=map(float,input().split())
    where.append((x,y))
for i in range(n):
    for j in range(i+1,n):
        temp=((where[j][0]-where[i][0])**2+(where[j][1]-where[i][1])**2)**0.5
        heappush(heap,(temp,i,j))
while n!=1:
    c,a,b=heappop(heap)
    q=find(a)
    w=find(b)
    if q!=w:
        merge(q,w)
        ans+=c
        n-=1
print(round(ans,2))