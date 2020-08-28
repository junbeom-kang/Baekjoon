import sys
import bisect
input=sys.stdin.readline
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
        a=bisect.bisect_left(ans,i)
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