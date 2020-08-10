import sys
from heapq import *
input=sys.stdin.readline
n=int(input())
leftheap=[]
rightheap=[]
first=int(input())
heappush(leftheap,-first)
print(first)
for i in range(1,n):
    temp=int(input())
    if i%2==1:
        leftmax=-heappop(leftheap)
        if temp<leftmax:
            heappush(leftheap,-temp)
            heappush(rightheap,leftmax)
        else:
            heappush(rightheap,temp)
            heappush(leftheap,-leftmax)
    else:
        rightmin=heappop(rightheap)
        if temp>rightmin:
            heappush(leftheap,-rightmin)
            heappush(rightheap,temp)
        else:
            heappush(leftheap,-temp)
            heappush(rightheap,rightmin)
    x = heappop(leftheap)
    print(-x)
    heappush(leftheap, x)
