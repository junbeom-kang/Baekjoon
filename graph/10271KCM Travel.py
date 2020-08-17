import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline

n,m,k=map(int,input().split())
adj=[[]for _ in range(n+1)]
for _ in range(k):
    a,b,c,d=map(int,input().split())
    adj[a].append((b,c,d))
#def dfs

#dp

#print(dp[m])