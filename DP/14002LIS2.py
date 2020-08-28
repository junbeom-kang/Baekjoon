import sys
input=sys.stdin.readline
n=int(input())
stack=list(map(int,input().split()))
ans=[0 for _ in range(n)]
for i in range(0,n):
    for j in range(0,i):
        if stack[i]>stack[j] and ans[i]<ans[j]:
            ans[i]=ans[j]
    ans[i]+=1
a=max(ans)
print(a)
temp=ans.index(a)
A=[stack[temp]]
for i in range(temp-1,-1,-1):
    if ans[i]==a-1 and stack[i]<stack[temp]:
        A.append(stack[i])
        a-=1
print(*A[::-1])