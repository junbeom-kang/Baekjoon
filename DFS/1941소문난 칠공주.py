import sys
input=sys.stdin.readline
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def solution():
    global cnt,q,w
    def dfs(x,y):
        global cnt,q,w
        if w==4:
            return
        if q+w==7:
            print(x,y,q,w,"!!!!")
            cnt+=1
            return
        for t in range(4):
            nx=x+dx[t]
            ny=y+dy[t]
            if 0<=nx<5 and 0<=ny<5:
                if not visited[nx][ny] and not temp[nx][ny]:
                    temp[nx][ny] = True
                    if arr[nx][ny]=='Y':
                        dfs(nx,ny)
                    else:
                        dfs(nx,ny)
                    temp[nx][ny]=False
    cnt=0
    arr=[]
    for _ in range(5):
        arr.append(list(input().rstrip()))
    visited=[[False]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            temp = [[False] * 5 for _ in range(5)]
            temp[i][j]=True
            q,w=0,0
            if arr[i][j]=='Y':
                w=1
                dfs(i,j)
            else:
                q=1
                dfs(i,j)
            visited[i][j]=True
    print(cnt)
    return

if __name__ == '__main__':
    solution()

