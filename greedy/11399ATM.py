import sys
input=sys.stdin.readline
n=int(input())
ans=[0]*n
stack=list(map(int,input().split()))
stack.sort()
ans[0]=stack[0]
sum=0
for i in range(1,n):
    ans[i]=ans[i-1]+stack[i]
for i in range(n):
    sum+=ans[i]
print(sum)