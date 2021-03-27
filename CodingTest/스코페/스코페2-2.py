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
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n=int(input())
dic={}
cnt=0
parent=[i for i in range(n)]
adj=[[]for _ in range(n)]
Q=[]
for i in range(n):
    a,b,c=input().split()
    if a not in dic:
        dic[a]=cnt
        cnt+=1
    if b not in dic:
        dic[b]=cnt
        cnt+=1
    heappush(Q,(int(c),dic[a],dic[b]))
L=cnt
t=1
ans=0
while t<cnt:
    c,a,b,=heappop(Q)
    q=find(a)
    w=find(b)
    if q!=w:
        merge(q,w)
        ans+=c
        t+=1
print(ans)