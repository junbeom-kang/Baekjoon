from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def solution(places):
    answer = []
    for i in range(5):
        answer.append(check(places[i]))
    return answer


def check(place):
    visited=[[False]*5 for _ in range(5)]
    P=[]
    for i in range(5):
        for j in range(5):
            if place[i][j]=="P":
                P.append((i,j))
    for x,y in P:
        can=BFS(x,y,place,visited)
        if not can:
            return 0
    return 1

def BFS(x,y,place,visited):
    Q=deque([(x,y,0)])
    visited[x][y] = True
    while Q:
        a,b,c= Q.popleft()
        if c==2:
            return True
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if nx<0 or nx>4 or ny<0 or ny>4:
                continue
            if not visited[nx][ny]:
                if place[nx][ny]=="P":
                    return False
                elif place[nx][ny]=="O":
                    visited[nx][ny]=True
                    Q.append((nx,ny,c+1))


    return True
if __name__ == '__main__':
    print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))



