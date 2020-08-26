import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
adj=[[]for _ in range(n+1)]
for _ in range(n-1):
    a,b,c=map(int,input().split())
    adj[a].append((b,c))
    adj[b].append((a,c))
def bfs(v,dist):
    dist[v]=0
    Q=deque([(v,0)])
    while Q:
        a,b=Q.popleft()
        for c,d in adj[a]:
            if dist[c]==-1:
                dist[c]=b+d
                Q.append((c,b+d))
    return

dist=[-1]*(n+1)
bfs(1,dist)

index=dist.index(max(dist))
dist=[-1]*(n+1)
bfs(index,dist)
print(max(dist))