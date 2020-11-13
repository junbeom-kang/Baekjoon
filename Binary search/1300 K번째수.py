import sys
input=sys.stdin.readline
n=int(input())
k=int(input())
def check(mid):
    cnt=0
    for i in range(1,n+1):
        cnt+=min(mid//i,n)
    return cnt


def BinarySearch():
    ans=0
    left=1
    right=n**2
    while left<=right:
        mid=(left+right)//2
        if check(mid)>=k:
            ans=mid
            right=mid-1
        else:
            left=mid+1
    return ans



print(BinarySearch())