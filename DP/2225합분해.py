import sys
input=sys.stdin.readline
n,m=map(int,input().split())
dp=[[0]*(m+1) for _ in range(n+1)]
for i in range(1,m+1):
    dp[0][i]=1
for i in range(1,n+1):
    for j in range(1,m+1):
        temp=0
        for k in range(1,j+1):
            temp+=dp[i-1][k]
        dp[i][j]=temp

print(dp[n][m]%1000000000)