import sys
input=sys.stdin.readline
first=list(input().rstrip())
second=list(input().rstrip())
lf=len(first)
ls=len(second)
dp=[[0]*(lf+1)for _ in range(ls+1)]
for i in range(1,ls+1):
    for j in range(1,lf+1):
        if first[j-1]==second[i-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            print(dp[i-1][j],dp[i][j-1])
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[ls][lf])
