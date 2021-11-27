dx=[0,1,0,-1,0,-1,0,1]
dy=[-1,0,1,0,-1,0,1,0]
def solution(n, m):
    global cnt,time
    def DFS(x,y):
        global cnt,time
        answer[x][y]=time
        visited[x][y]=True
        nx=x+dx[cnt]
        ny=y+dy[cnt]
        if not(0<=nx<n and 0<=ny<m) or visited[nx][ny]:
            cnt=(cnt+1)%8
            nx = x + dx[cnt]
            ny = y + dy[cnt]
            if cnt==3 or cnt==7:
                cnt=(cnt+1)%8

        time+=1
        if time<=n*m:
            DFS(nx,ny)

    time=1
    cnt=0
    visited=[[False]*m for _ in range(n)]
    answer =[[0]*m for _ in range(n)]
    DFS(0,m-1)
    return answer










if __name__ == '__main__':
    solution(8,6)