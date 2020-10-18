import sys
from collections import deque
input=sys.stdin.readline
def BFS():
    day=1
    F=deque(fire)
    S=deque(start)
    while S:
        for _ in range(len(F)):
            a,b=F.popleft()
            for na,nb in (a+1,b),(a-1,b),(a,b+1),(a,b-1):
                if na<0 or na>=n or nb<0 or nb>=m:
                    continue
                if adj[na][nb]=='.':
                    adj[na][nb]='*'
                    F.append((na,nb))
        for t in range(len(S)):
            a,b=S.popleft()
            for na, nb in (a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1):
                if na<0 or na>=n or nb<0 or nb>=m:
                    return day
                if adj[na][nb]=='.':
                    adj[na][nb]='@'
                    S.append((na,nb))
        day+=1
    return 'IMPOSSIBLE'

T=int(input())
for _ in range(T):
    m,n=map(int,input().split())
    adj=[list(input().rstrip()) for _ in range(n)]
    start=[]
    fire=[]
    for i in range(n):
        for j in range(m):
            if adj[i][j]=='*':
                fire.append((i,j))
            elif adj[i][j]=='@':
                start.append((i,j))
    print(BFS())
