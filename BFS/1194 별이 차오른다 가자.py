import sys
from collections import deque
input=sys.stdin.readline
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def BFS():
    cnt=0
    Q = deque([(start, 0)])
    while Q:
        for i in range(len(Q)):
            temp,bit=Q.popleft()
            for d in range(4):
                nx=temp[0]+dx[d]
                ny=temp[1]+dy[d]
                if 0<=nx<n and 0<=ny<m:
                    if adj[nx][ny]=='#':
                        continue
                    elif adj[nx][ny]=='.'or adj[nx][ny]=='0':
                        if not visited[bit][nx][ny]:
                            visited[bit][nx][ny]=1
                            Q.append(((nx,ny),bit))
                    elif adj[nx][ny]=='1':
                        return cnt+1
                    else:
                        if ord(adj[nx][ny])>94:
                            if not visited[bit][nx][ny]:
                                visited[bit][nx][ny]=1
                                Q.append(((nx,ny),bit|(1<<(ord(adj[nx][ny])-ord('a')))))
                        else:
                            if bit&(1<<(ord(adj[nx][ny])-ord('A'))):
                                if not visited[bit][nx][ny]:
                                    visited[bit][nx][ny]=1
                                    Q.append(((nx,ny),bit))
        cnt+=1
    return -1



n,m=map(int,input().split())
adj=[list(input().rstrip()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if adj[i][j]=='0':
            start=(i,j)
            break
visited=[[[0]*m for i in range(n)]for _ in range(1<<6)]
print(BFS())
