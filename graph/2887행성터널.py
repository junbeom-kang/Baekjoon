import sys
from heapq import *
def find(v):
    if parent[v]==v:
        return v
    else:
        parent[v]=find(parent[v])
        return parent[v]

def merge(a,b):
    if q<w:
        parent[w]=q
    else:
        parent[q]=w

input=sys.stdin.readline
n=int(input())
parent=[i for i in range(n)]
heap=[]
ans=0
where=[[]for _ in range(3)]
for i in range(n):
    a,b,c=map(int,input().split())
    where[0].append((a,i))
    where[1].append((b,i))
    where[2].append((c,i))
where[0].sort()
where[1].sort()
where[2].sort()
for i in range(3):
    for j in range(n-1):
        temp=abs(where[i][j][0]-where[i][j+1][0])
        heappush(heap,(temp,where[i][j][1],where[i][j+1][1]))
while n!=1:
    temp,a,b=heappop(heap)
    q=find(a)
    w=find(b)
    if q!=w:
        merge(q,w)
        n-=1
        ans+=temp
print(ans)


