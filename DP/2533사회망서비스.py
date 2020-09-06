import sys
sys.setrecursionlimit(10**9)
def dfs(v):
    visited[v]=1
    for i in adj[v]:
        if visited[i]==-1:
            dfs(i)
            dp[v][1]+=min(dp[i][0],dp[i][1])
            dp[v][0]+=dp[i][1]
    dp[v][1]+=1

input=sys.stdin.readline
n=int(input())
dp=[[0]*2 for _ in range(n+1)]
adj=[[]for _ in range(n+1)]
visited=[-1]*(n+1)
for _ in range(n-1):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
dfs(1)
print(min(dp[1]))