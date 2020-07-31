import sys
input=sys.stdin.readline
n=int(input())
stack=list(map(int,input().split()))
stack1=stack[::-1]
dp=[0 for _ in range(n)]
dp1=[0 for _ in range(n)]
def find(stack,dp):
    for i in range(0, n):
        for j in range(0, i):
            if stack[i] > stack[j]:
                if dp[i] < dp[j]:
                    dp[i] = dp[j]
        dp[i] += 1

find(stack,dp)
find(stack1,dp1)
ans1=[]
for i in range(n):
    ans1.append(dp[i]+dp1[n-1-i])
print(max(ans1)-1)