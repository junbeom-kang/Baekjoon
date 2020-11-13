import sys
input=sys.stdin.readline
n,c=map(int,input().split())
stack=[]
for i in range(n):
    stack.append(int(input()))
stack.sort()

def check(mid):
    cnt=1
    cnt1=1
    temp=stack[0]
    temp1=stack[-1]
    for i in range(1,len(stack)):
        if stack[i]>=temp+mid:
            temp=stack[i]
            cnt+=1
    for i in range(len(stack)-2,-1,-1):
        if stack[i]<=temp1-mid:
            temp1=stack[i]
            cnt1+=1
    if (cnt,cnt1)>=c:
        return True
    else:
        return False

def BinarySearch():
    ans=0
    left=1
    right=stack[-1]
    while left<=right:
        mid=(left+right)//2
        if check(mid):
            ans=mid
            left=mid+1
        else:
            right=mid-1
    return ans


print(BinarySearch())