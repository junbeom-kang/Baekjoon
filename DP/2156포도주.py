import sys
input=sys.stdin.readline
n=int(input())
dp=[0 for i in range(n)]
stack=[]
for i in range(n):
    stack.append(int(input()))

if n == 1:
    print(stack[n-1])
elif n==2:
    print(stack[n-1]+stack[n-2])
else:
    dp[0]=stack[0]
    dp[1]=dp[0]+stack[1]
    dp[2]=sum(stack[0:3])-min(stack[0:3])

    for i in range(3,n):
        case1=stack[i]+stack[i-1]+dp[i-3]
        case2=stack[i]+dp[i-2]
        case3=dp[i-1]
        dp[i]=max(case1,case2,case3)
    print(dp[n-1])