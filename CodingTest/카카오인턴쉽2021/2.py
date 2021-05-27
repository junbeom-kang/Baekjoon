import sys
from collections import deque
input=sys.stdin.readline
temp=[["OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
dx=[0,0,-1,1]
dy=[1,-1,0,0]

def solution(places):
    answer = []
    for temp1 in places:
        can = 1

        zz = [[0] * 5 for _ in range(5)]
        P = []
        can = 1
        for i in range(5):
            for j in range(5):
                if temp1[i][j] == 'P':
                    P.append((i, j))
                zz[i][j] = temp1[i][j]
        for i in P:
            can = BFS(i[0],i[1],zz)
            if can==0:
                break
        answer.append(can)
    return answer
def BFS(a,b,zz):
    cnt=0
    Q=deque([])
    Q.append((a,b))
    while Q and cnt<3:
        for i in range(len(Q)):
            x,y=Q.popleft()
            if zz[x][y]=='P' and (x!=a or y!=b):
                return 0
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<5 and 0<=ny<5:
                    if zz[nx][ny]!='X':
                        Q.append((nx,ny))
        cnt+=1
    return 1

print(solution(temp))

