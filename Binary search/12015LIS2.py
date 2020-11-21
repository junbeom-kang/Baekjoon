import sys
input=sys.stdin.readline
n=int(input())
stack=list(map(int,input().split()))
ans=[stack[0]]
for i in stack[1:]:
    check=False
    left=0
    right=len(ans)-1
    while left<=right:
        mid=(left+right)//2
        if i<=ans[mid]:
            temp=mid
            right=mid-1
            check=True
        else:
            left=mid+1
    if check:
        ans[temp]=i
    else:
        ans.append(i)


print(len(ans))
