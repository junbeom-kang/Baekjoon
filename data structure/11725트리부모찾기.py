import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
n=int(input())
visit=[False]*(n+1)
adj=[[]for _ in range(n+1)]
ans=[0]*(n+1)
for i in range(n-1):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
def dfs(v):
    visit[v]=True
    for i in adj[v]:
        if not visit[i]:
            ans[i]=v
            dfs(i)
dfs(1)
for i in ans[2:]:
    print(i)