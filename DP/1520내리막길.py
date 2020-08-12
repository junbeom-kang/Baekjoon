import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline
n,m=map(int,input().split())
dx=[0,0,1,-1]
dy=[1,-1,0,0]
dp=[[0 for _ in range(m)]for _ in range(n)]
check=[[False for _ in range(m)]for _ in range(n)]
dp[n-1][m-1]=1
adj=[]
for i in range(n):
    adj.append(list(map(int,input().split())))

def dfs(x,y):
    if check[x][y]:
        return dp[x][y]
    else:
        for d in range(4):
            rx=x+dx[d]
            ry=y+dy[d]
            if 0<=rx<n and 0<=ry<m:
                if adj[rx][ry]<adj[x][y]:
                    dp[x][y]+=dfs(rx,ry)
    check[x][y]=True
    return dp[x][y]


print(dfs(0,0))