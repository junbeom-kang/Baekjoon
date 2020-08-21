import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000)
INF=sys.maxsize
n=int(input())
adj=[list(map(int,input().split()))for _ in range(n)]
dp=[[INF]*(1<<n)for _ in range(n)]
def dfs(current,visit):
    if visit==(1<<n)-1:
        if adj[current][0]==0:
            return INF
        else:
            return adj[current][0]
    if dp[current][visit]!=INF:
        return dp[current][visit]
    for i in range(1,n):
        if not visit&(1<<i) and adj[current][i]!=0:
            dp[current][visit]=min(dp[current][visit],dfs(i,visit|(1<<i))+adj[current][i])
    return dp[current][visit]
print(dfs(0,1))