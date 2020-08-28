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
reverse=[]
num=0
for i in stack:
    if i>ans[-1]:
        ans.append(i)
        reverse.append(len(ans)-1)
    else:
        a=bs(i)
        ans[a]=i
        reverse.append(a)
    num += 1
temp=len(ans)
print(temp)
A=[]
for i in range(len(reverse)-1,-1,-1):
    if reverse[i]==temp-1:
        A.append(stack[i])
        temp-=1
print(*A[::-1])