import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline
dx=[0,0,-1,1]
dy=[1,-1,0,0]

def dfs(i, j):
    check[i][j] = True
    for k in range(4):
        rx = i + dx[k]
        ry = j + dy[k]
        if 0 <= rx < n and 0 <= ry < m:
            if not check[rx][ry] and adj[rx][ry]==1:
                dfs(rx, ry)
T=int(input())
for _ in range(T):
    ans=0
    m,n,k=map(int,input().split())
    check=[[False for _ in range(m)]for _ in range(n)]
    adj=[[0 for _ in range(m)]for _ in range(n)]
    for _ in range(k):
        a,b=map(int,input().split())
        adj[b][a]=1
    for i in range(n):
        for j in range(m):
            if adj[i][j]==1 and not check[i][j]:
                dfs(i,j)
                ans+=1
    print(ans)