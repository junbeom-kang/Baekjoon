import sys
input=sys.stdin.readline
n=int(input())
stack=[]
for _ in range(n):
    stack.append(int(input()))
stack.sort()
ans=0
cnt=len(stack)
for i in stack:
    ans=max(i*cnt,ans)
    cnt-=1
print(ans)