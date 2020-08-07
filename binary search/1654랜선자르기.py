import sys
input=sys.stdin.readline
k,n=map(int,input().split())
stack=[]
for i in range(k):
    stack.append(int(input()))
ans=0
def check(mid):
    cnt=0
    for i in stack:
        cnt+=i//mid
    if cnt>=n:
        return True
    else:
        return False

def UpperBound():
    left=1        ##0으로하면 런타임에러 0으로 나누는 경우때문에
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