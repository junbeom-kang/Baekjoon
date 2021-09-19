import sys
from itertools import combinations
input=sys.stdin.readline

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def solution(n,m,arr):
    global size
    def DFS(x, y):
        global size
        visited[x][y]=True
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny]==0:
                    t.add((nx,ny))
                if not visited[nx][ny] and arr[nx][ny]==2:
                    size+=1
                    DFS(nx,ny)

    answer=0
    visited=[[False]*m for _ in range(n)]
    setList=[]
    numList=set()
    for i in range(n):
        for j in range(m):
            if arr[i][j]==2 and not visited[i][j]:
                t=set()
                size=1
                DFS(i,j)
                if len(t)<=2:
                    setList.append((t,size))
                    for k in t:
                        numList.add(k)
    if len(numList)==1:
        tt=0
        for i in setList:
            tt+=i[1]
        print(tt)
    else:
        for a,b in combinations(numList,2):
            cnt=0
            temp= {a,b}
            for i in setList:
                if len(i[0]-temp)==0:
                    cnt+=i[1]
            answer=max(answer,cnt)
        print(answer)









if __name__ == '__main__':
    n,m=map(int,input().split())
    arr=[]
    for i in range(n):
        arr.append(list(map(int,input().split())))
    solution(n,m,arr)