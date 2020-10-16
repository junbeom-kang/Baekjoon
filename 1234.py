import sys
from collections import deque
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
def DFS(c,d):
    print(c,d)
    global count
    if c>n or d>m:
        return
    if adj[c+1][d]>0 and visited[c+1][d]==0:
        visited[c + 1][d] = 1
        count+=1
        DFS(c+1,d)
    if adj[c-1][d]>0 and visited[c-1][d]==0:
        visited[c-1][d]=1
        count+=1
        DFS(c-1,d)
    if adj[c][d+1]>0 and visited[c][d+1]:
        visited[c][d+1]=1
        count+=1
        DFS(c,d+1)
    if adj[c][d-1]>0 and visited[c][d-1]:
        visited[c][d-1]=1
        count+=1
        DFS(c,d-1)

n,m=map(int,input().split())
visited=[[0]*(m+2) for _ in range(n+2)]
adj=[[-1]*(m+2)]
for i in range(n):
    adj.append([-1]+list(map(int,input().split()))+[-1])
adj.append([-1]*(m+2))
zero=[]
ice=set()
for i in range(1,n+1):
    for j in range(1,m+1):
        if adj[i][j]==0:
            zero.append((i,j))
        else:
            ice.add((i,j))
Q=deque(zero)
day=0
while Q:
    for t in range(len(Q)):
        a,b=Q[t][0],Q[t][1]
        if adj[a+1][b]==1:
            Q.append((a+1,b))
            ice.remove((a+1,b))
        adj[a+1][b]-=1
        if adj[a][b+1]==1:
            Q.append((a,b+1))
            ice.remove((a,b+1))
        adj[a][b+1]-=1
        if adj[a-1][b]==1:
            Q.append((a-1,b))
            ice.remove((a-1,b))
        adj[a-1][b]-=1
        if adj[a][b-1]==1:
            Q.append((a,b-1))
            ice.remove((a,b-1))
        adj[a][b-1]-=1
    day+=1
    count=0
    if ice:
        for q,w in ice:
            print(q,w)
            visited[q][w]=0
        for c,d in ice:
            visited[c][d]=1
            DFS(c,d)
            break
        if count!=len(ice):
            break
    else:
        break
print(day)