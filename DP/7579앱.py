import sys
input=sys.stdin.readline
n,m=map(int,input().split())
data=list(map(int,input().split()))
cost=list(map(int,input().split()))
sc=sum(cost)
dp=[[0 for _ in range(n+1)]for _ in range(sc+2)]

for i in range(1,sc+2):
    for j in range(1,n+1):
        if cost[j-1]<=i-1:
            dp[i][j]=max(data[j-1]+dp[i-cost[j-1]][j-1],dp[i][j-1])
        else:
            dp[i][j]=dp[i][j-1]
        if dp[i][j]>=m:
            print(i-1)
            sys.exit()
