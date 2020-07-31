import sys
input=sys.stdin.readline
n=int(input())
stack=list(map(int,input().split()))
ans=[0 for _ in range(n)]
for i in range(0,n):
    for j in range(0,i):
        if stack[i]>stack[j]:
            if ans[i]<ans[j]:
                ans[i]=ans[j]
    ans[i]+=1
print(ans)
print(max(ans))