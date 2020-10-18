import sys
from collections import deque
input=sys.stdin.readline
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def BFS():
    day=1
    F=deque(fire)
    S=deque(start)
    while S:
        for _ in range(len(F)):
            a,b=F.popleft()
            for d in range(4):
                na=a+dx[d]
                nb=b+dy[d]
                if na < 0 or na >= n or nb < 0 or nb >= m:
                    continue
                if adj[na][nb] == '.':
                    adj[na][nb] = '*'
                    F.append((na, nb))
        for t in range(len(S)):
            q,w=S.popleft()
            for d in range(4):
                na=q+dx[d]
                nb=w+dy[d]
                if na < 0 or na >= n or nb < 0 or nb >= m:
                    return day
                if adj[na][nb] == '.':
                    adj[na][nb] = '@'
                    S.append((na, nb))
        day+=1
    return 'IMPOSSIBLE'

T=int(input())
for _ in range(T):
    m,n=map(int,input().split())
    adj=[list(input().rstrip()) for _ in range(n)]
    start=[]
    empty=[]
    fire=[]
    for i in range(n):
        for j in range(m):
            if adj[i][j]=='*':
                fire.append((i,j))
            elif adj[i][j]=='@':
                start.append((i,j))
    print(BFS())
