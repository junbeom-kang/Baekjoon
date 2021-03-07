import sys
from heapq import *
input=sys.stdin.readline
INF=sys.maxsize
def dijkstra():
    while Q:
        weight,num=heappop(Q)
        if temp[num]!=weight:
            continue
        else:
            for q,w in arr[num]:
                if temp[q]>weight+w:
                    temp[q]=weight+w
                    heappush(Q,(weight+w,q))


n,m,k=map(int,input().split())
arr=[[] for _ in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    arr[b].append((a,c))
where=list(map(int,input().split()))
temp=[float('inf')]*(n+1)
Q=[]
for i in where:
    temp[i]=0
    Q.append((0,i))
dijkstra()

M = max(temp[1:])
for i in range(1,n+1):
    if temp[i]==M:
        print(i)
        print(M)
        break