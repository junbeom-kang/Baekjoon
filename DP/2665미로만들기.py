import sys
from heapq import *
INF=10000
dx=[0,0,1,-1]
dy=[1,-1,0,0]
input=sys.stdin.readline
n=int(input())
adj=[list(map(int,input().rstrip()))for _ in range(n)]
visited=[[-1]*n for _ in range(n)]
dp=[[INF]*n for _ in range(n)]
dp[0][0]=0
Q=[]
heappush(Q,(0,0,0))
visited[0][0]=1
while Q:
    c,a,b=heappop(Q)
    for w in range(4):
        na=a+dx[w]
        nb=b+dy[w]
        if na<0 or na>=n or nb<0 or nb>=n:
            continue
        if visited[na][nb]==1:
            continue
        if adj[na][nb]==1:
            if dp[a][b]<dp[na][nb]:
                dp[na][nb]=dp[a][b]
                heappush(Q,((c,na,nb)))
        else:
            if c+1<dp[na][nb]:
                dp[na][nb]=c+1
                heappush(Q, ((c+1, na, nb)))
print(dp[n-1][n-1])