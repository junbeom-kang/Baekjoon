import sys
input=sys.stdin.readline
n=int(input())
dp=[[0,0,0]for _ in range(100001)]
dp[1][0]=1
dp[2][1]=1
dp[3]=[1,1,1]
p=1000000009
for i in range(4,100001):
    dp[i][2]=(dp[i-3][0]+dp[i-3][1])%p
    dp[i][1]=(dp[i-2][0]+dp[i-2][2])%p
    dp[i][0]=(dp[i-1][1]+dp[i-1][2])%p
for i in range(n):
    t=int(input())
    print(sum(dp[t])%p)
