import sys
input=sys.stdin.readline
n=int(input())
k=int(input())
if k>n//2:
    print(0)
    sys.exit()
if k==1:
    print(n)
    sys.exit()
dp=[[0]*(k+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][1]=i
for i in range(3,n+1):
    for j in range(2,k+1):
        dp[i][j]=dp[i-2][j-1]+dp[i-1][j]

ans=(dp[n-1][k]+dp[n-3][k-1])%1000000003
print(ans)