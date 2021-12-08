import sys
from collections import deque
input=sys.stdin.readline
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def solution(grid):
    answer=0
    n=len(grid)
    m=len(grid[0])
    visited=[[False]*m for _ in range(n)]
    Q=deque([])
    for i in range(n):
        for j in range(m):
            if grid[i][j]==0:
                Q.append((i,j,0))
                visited[i][j]=True
    while Q:
        lq=len(Q)
        for j in range(lq):
            x,y,w=Q.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                    Q.append((nx,ny,w+1))
                    visited[nx][ny]=True
            answer=w
    return answer

if __name__ == '__main__':
    solution([[0,0,1,1,1],[1,0,0,1,1],[0,0,0,0,1],[0,0,1,0,1],[0,0,1,0,1]])
    solution([[0,1,1,1,1],[1,1,1,1,1,1],[0,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])


