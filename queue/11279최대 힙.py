import sys
from heapq import*
input=sys.stdin.readline
n=int(input())
plus_heap=[]
minus_heap=[]
for _ in range(n):
    i=int(input())
    if i==0:
        if plus_heap and minus_heap:
            a,b=heappop(plus_heap),heappop(minus_heap)
            if a<b:
                print(a)
                heappush(minus_heap,b)
            else:
                print(-b)
                heappush(plus_heap,a)
        elif plus_heap:
            print(heappop(plus_heap))
        elif minus_heap:
            print(-heappop(minus_heap))
        else:
            print(0)
    else:
        if i>0:
            heappush(plus_heap,i)
        else:
            heappush(minus_heap,-i)
