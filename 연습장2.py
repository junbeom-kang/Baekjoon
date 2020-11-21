import sys
from bisect import bisect
input=sys.stdin.readline
def BS(m):
    left=0
    right=m
    limit=0
    ans=0
    while left<=right:
        temp=0
        mid=(left+right)//2
        for i in data:
            if i>mid:
                temp+=mid
            else:
                temp+=i
            if temp>m:
                break
        if temp<=m:
            ans=max(temp,ans)
            limit=mid
            left=mid+1
        else:
            right=mid-1
    return limit




n=int(input())
data=list(map(int,input().split()))
m=int(input())

if sum(data)<=m:
    print(max(data))
else:
    print(BS(m))