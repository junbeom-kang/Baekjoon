import sys
input=sys.stdin.readline
def bs(v):
    left=0
    right=len(ans)-1
    while left<=right:
        mid=(left+right)//2
        if v<=ans[mid]:
            temp=mid
            right=mid-1
        elif v>ans[mid]:
            left=mid+1
    return temp

n=int(input())
stack=list(map(int,input().split()))
ans=[stack[0]]
for i in stack:
    if i>ans[-1]:
        ans.append(i)
    else:
        ans[bs(i)]=i
print(len(ans))