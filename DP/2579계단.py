import sys
input=sys.stdin.readline
n=int(input())
stack=[[]for _ in range(n)]
ans=[]
for i in range(n):
    stack[i]=int(input())
if n == 1:
    print(stack[n-1])
elif n==2:
    print(stack[n-1]+stack[n-2])
else:
    ans.append(stack[0])
    ans.append(ans[0]+stack[1])
    ans.append(max(stack[0]+stack[2],stack[1]+stack[2]))
    for i in range(3,n):
        ans.append(max(stack[i]+stack[i-1]+ans[i-3],stack[i]+ans[i-2]))
    print(ans[n-1])