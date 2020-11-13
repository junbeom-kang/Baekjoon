from heapq import *
import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
beer=[]
P=True
for _ in range(k):
    beer.append(tuple(map(int,input().split())))
beer.sort(key= lambda x:(x[1],-x[0]))
heap=[]
sum=0
for i,j in beer:
    heappush(heap,i)
    sum+=i
    if len(heap)>n:
        sum-=heappop(heap)
    if len(heap)==n and sum>=m:
        print(j)
        P=False
        break
if P:
    print(-1)


