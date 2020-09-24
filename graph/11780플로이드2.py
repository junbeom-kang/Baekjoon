import sys
input=sys.stdin.readline
INF=sys.maxsize
n=int(input())
m=int(input())
adj=[[INF for _ in range(n+1)]for _ in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    if c<adj[a][b]:
        adj[a][b]=c
way=[[[]for _ in range(n+1)]for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            continue
        else:
            way[i][j]=[i,j]
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                adj[i][j]=0
                continue
            if adj[i][j]>adj[i][k]+adj[k][j]:
                adj[i][j]=adj[i][k]+adj[k][j]
                way[i][j]=way[i][k]+way[k][j][1:]
for i in adj[1:]:
    print(*i[1:])
for i in way[1:]:
    for j in i[1:]:
        if j:
            print(len(j),*j)
        else:
            print(0)