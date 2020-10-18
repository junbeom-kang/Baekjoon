import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
def DFS(c,d):
    visited[c][d] = 1
    global count
    if c>n or d>m:
        return
    if adj[c+1][d]>0 and visited[c+1][d]==0:
        count+=1
        DFS(c+1,d)
    if adj[c-1][d]>0 and visited[c-1][d]==0:
        count+=1
        DFS(c-1,d)
    if adj[c][d+1]>0 and visited[c][d+1]==0:
        count+=1
        DFS(c,d+1)
    if adj[c][d-1]>0 and visited[c][d-1]==0:
        count+=1
        DFS(c,d-1)

n,m=map(int,input().split())
visited=[[-1]*(m+2) for _ in range(n+2)]
adj=[[-1]*(m+2)]
for i in range(n):
    adj.append([-1]+list(map(int,input().split()))+[-1])
adj.append([-1]*(m+2))
ice=set()
can=False
for i in range(1,n+1):
    for j in range(1,m+1):
        if adj[i][j]>0:
            ice.add((i,j))

day=0
while ice:
    temp=set()
    for t in ice:
        a,b=t[0],t[1]
        if adj[a+1][b]==0 and (a+1,b) not in ice:
            adj[a][b]-=1
            if adj[a][b]==0:
                temp.add((a,b))
        if adj[a][b+1]==0 and (a,b+1) not in ice:
            adj[a][b] -= 1
            if adj[a][b] == 0:
                temp.add((a, b))
        if adj[a-1][b]==0 and (a-1,b) not in ice:
            adj[a][b] -= 1
            if adj[a][b] == 0:
                temp.add((a, b))
        if adj[a][b-1]==0 and (a,b-1) not in ice:
            adj[a][b] -= 1
            if adj[a][b] == 0:
                temp.add((a, b))
    for r,t in temp:
        adj[r][t]=0

    ice=ice-temp
    day+=1
    count=1
    if ice:
        for q,w in ice:
            visited[q][w]=0
        for c,d in ice:
            DFS(c,d)
            break
        if count!=len(ice):
            can=True
            break
    else:
        break
if can:
    print(day)
else:
    print(0)