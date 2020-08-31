import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
n=int(input())
w=int(input())
adj=[]
dp=[[-1]*(w+1) for _ in range(w+1)]
for i in range(w):
    adj.append(list(map(int,input().split())))


def DP(x,y):
    if dp[x][y]!=-1:
        return dp[x][y]
    if x==w or y==w:
        dp[x][y]=0
        return dp[x][y]
    dp[x][y]=0
    temp=max(x,y)+1
    if x==0 and y==0:
        dp[x][y] = min(DP(temp, y) + abs(adj[temp - 1][0] - 1) + abs(adj[temp - 1][1] - 1),
                       DP(x, temp) + abs(adj[temp - 1][0] - n) + abs(adj[temp - 1][1] - n))
    elif x==0:
        dp[x][y] = min(DP(temp, y) + abs(adj[temp - 1][0] - 1) + abs(adj[temp - 1][1] - 1),
                       DP(x,temp)+abs(adj[temp-1][0]-adj[y-1][0])+abs(adj[temp-1][1]-adj[y-1][1]))
    elif y==0:
        dp[x][y] = min(DP(temp, y) + abs(adj[temp - 1][0] - adj[x - 1][0]) + abs(adj[temp - 1][1] - adj[x - 1][1]),
                       DP(x, temp) + abs(adj[temp - 1][0] - n) + abs(adj[temp - 1][1] - n))
    else:
        dp[x][y]=min(DP(temp,y)+abs(adj[temp-1][0]-adj[x-1][0])+abs(adj[temp-1][1]-adj[x-1][1]),
                     DP(x,temp)+abs(adj[temp-1][0]-adj[y-1][0])+abs(adj[temp-1][1]-adj[y-1][1]))
    return dp[x][y]
DP(0,0)
print(dp[0][0])
a=0
b=0
ans=[]
for i in range(w):
    temp=max(a,b)+1
    if a==0 and b==0:
        if dp[0][1]+abs(adj[temp-1][0]-n)+abs(adj[temp-1][1]-n)>=dp[1][0]+abs(adj[temp-1][0]-1)+abs(adj[temp-1][1]-1):
            ans.append(1)
            a=temp
        else:
            ans.append(2)
            b=temp
    elif a==0:
        if dp[0][temp]+abs(adj[temp-1][0]-adj[b-1][0])+abs(adj[temp-1][1]-adj[b-1][1])>=dp[temp][b]+abs(adj[temp-1][0]-1)+abs(adj[temp-1][1]-1):
            a=temp
            ans.append(1)
        else:
            b=temp
            ans.append(2)
    elif b==0:
        if dp[temp][0]+abs(adj[temp-1][0]-adj[a-1][0])+abs(adj[temp-1][1]-adj[a-1][1])>=dp[a][temp]+abs(adj[temp-1][0]-n)+abs(adj[temp-1][1]-n):
            b=temp
            ans.append(2)
        else:
            a=temp
            ans.append(1)
    else:
        if dp[temp][b]+abs(adj[temp-1][0]-adj[a-1][0])+abs(adj[temp-1][1]-adj[a-1][1])>=dp[a][temp]+abs(adj[temp-1][0]-adj[b-1][0])+abs(adj[temp-1][1]-adj[b-1][1]):
            ans.append(2)
            b=temp
        else:
            a=temp
            ans.append(1)
for i in ans:
    print(i)
