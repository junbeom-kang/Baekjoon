import sys
from collections import deque
def input():
    return sys.stdin.readline()
dx=[0,0,1,-1,0,0]
dy=[0,0,0,0,1,-1]
dz=[1,-1,0,0,0,0]
M,N,H=map(int,input().split())
check=[[[-1]*M for i in range(N)]for j in range(H)] #날짜를 위해
arr=[[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
queue=deque()
for i in range(H):
    for j in range(N):
        for m in range(M):
            if arr[i][j][m]==0:
                continue
            else:
                check[i][j][m] = 0 #arr에서 -1이나 1일때는 이미 방문한곳으로
                if arr[i][j][m]==1:
                    queue.append([i,j,m])
#bfs
while queue:
    p,q,r=queue.popleft()
    for i in range(6):
        np=p+dz[i]
        nq=q+dy[i]
        nr=r+dx[i]
        if np<0 or np>=H or nq<0 or nq>=N or nr<0 or nr>=M:
            continue
        elif  check[np][nq][nr]==-1:
            check[np][nq][nr]=check[p][q][r]+1
            queue.append([np,nq,nr])
Max=max(sum(sum(check,[]),[])) #check 배열들을 합쳐서 최댓값을 구함
Min=min(sum(sum(check,[]),[])) #미치지 못한 곳 -1이 있으면 -1 출력
if Min==-1:
    print(-1)
else:
    print(Max)
