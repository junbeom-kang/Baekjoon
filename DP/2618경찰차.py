import sys
input=sys.stdin.readline
n=int(input())
w=int(input())
adj=[]
dp=[[-1]*(n+1) for _ in range(n+1)]
for i in range(w):
    adj.append(list(map(int,input().split())))





def DP(x,y):
    print(x,y)
    if dp[x][y]!=-1:
        return dp[x][y]
    if x==w or y==w:
        dp[x][y]=0
        return dp[x][y]
    dp[x][y]=0
    temp=max(x,y)+1
    if x==0 or y==0:
        dp[x][y] = min(DP(temp, y) + abs(adj[temp - 1][0] - 1) + abs(adj[temp - 1][1] - 1),
                       DP(x, temp) + abs(adj[temp - 1][0] - n) + abs(adj[temp - 1][1] - n))
    elif x==0:
        dp[x][y] = min(DP(temp, y) + abs(adj[temp - 1][0] - 1) + abs(adj[temp - 1][1] - 1),
                       DP(x,temp)+abs(adj[temp-1][0]-adj[y-1][0])+abs(adj[temp-1][1]-adj[y-1][1]))
    elif y==0:
        dp[x][y] = min(DP(temp, y) + abs(adj[temp - 1][0] - adj[x - 1][0]) + abs(adj[temp - 1][1] - adj[x - 1][1]),
                       DP(x, temp) + abs(adj[temp - 1][0] - n) + abs(adj[temp - 1][1] - n))
    else:
        dp[x][y]=min(DP(temp,y)+abs(adj[temp-1][0]-adj[x-1][0])+abs(adj[temp-1][1]-adj[x-1][1]),DP(x,temp)+abs(adj[temp-1][0]-adj[y-1][0])+abs(adj[temp-1][1]-adj[y-1][1]))
    return dp[x][y]
DP(0,0)
print(dp)
print(dp[0][0])

