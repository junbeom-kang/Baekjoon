import sys
input=sys.stdin.readline
n=int(input())
dp=list(map(int,input().split()))[:n]
for i in range(2,n+1):
    for j in range(1,i//2+1):
        dp[i-1]=min(dp[i-1],dp[j-1]+dp[i-j-1])
print(dp[n-1])