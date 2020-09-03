import sys
import math
sys.setrecursionlimit(5000)
from heapq import *
def merge(a,b):
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
def find(v):
    if parent[v]==v:
        return v
    else:
        parent[v]=find(parent[v])
        return parent[v]

input=sys.stdin.readline
n,m=map(int,input().split())
where=[]
heap=[]
parent=[i for i in range(n)]
for _ in range(n):
    a,b=map(int,input().split())
    where.append((a,b))
k=0
for _ in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    q=find(a)
    w=find(b)
    if q!=w:
        merge(q,w)
        k+=1

for i in range(n):
    for j in range(i+1,n):
        temp=math.sqrt((where[j][0]-where[i][0])**2+(where[j][1]-where[i][1])**2)
        heappush(heap,(temp,i,j))

ans=0
while k!=n-1:
    temp,a,b=heappop(heap)
    q=find(a)
    w=find(b)
    if q!=w:
        merge(q,w)
        ans+=temp
        k+=1
print("%0.2f" % ans)