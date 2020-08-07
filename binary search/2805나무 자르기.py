import sys
input=sys.stdin.readline
n,m=map(int,input().split())
stack=list(map(int,input().rstrip().split()))


def check(mid):
    cnt=0
    for i in stack:
        if i-mid>0:
            cnt+=i-mid
    if cnt>=m:
        return True
    else:
        return False


def UpperBound():
    ans=0
    left=0
    right=max(stack)
    while left<=right:
        mid=(left+right)//2
        if check(mid):
            ans=mid
            left=mid+1
        else:
            right=mid-1
    return ans


print(UpperBound())