import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
def dfs(v):
    visited[v]=1
    for i in adj[v]:
        if visited[i]==-1:
            dfs(i)
            dp[v][1]+=dp[i][0]
            dp[v][0]+=max(dp[i][0],dp[i][1])
    dp[v][1]+=w[v-1]

n=int(input())
w=list(map(int,input().split()))
adj=[[]for _ in range(n+1)]
dp=[[0]*2 for _ in range(n+1)]
visited=[-1]*(n+1)
for _ in range(n-1):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
dfs(1)
print(max(dp[1]))
