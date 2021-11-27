dx=[0,1,0,-1]
dy=[1,0,-1,0]

def solution(board, durability):
    global answer,cnt
    def change(nx,ny,num):
        global cnt,can
        if board[nx][ny]==1:
            if num==0:
                cnt=2
                can=False
            elif num==1:
                cnt=3
                can=False
            elif num==2:
                cnt=1
            elif num==3:
                cnt=0
        elif board[nx][ny]==2:
            if num==0:
                cnt=1
            elif num == 1:
                cnt = 3
                can=False
            elif num == 2:
                cnt = 0
                can=False
            elif num == 3:
                cnt = 2
        elif board[nx][ny]==3:
            if num==0:
                cnt=2
                can=False
            elif num==1:
                cnt=0
            elif num==2:
                cnt=3
            elif num==3:
                cnt=1
                can=False
        elif board[nx][ny]==4:
            if num==0:
                cnt=3
            elif num==1:
                cnt=2
            elif num==2:
                cnt=0
                can=False
            elif num==3:
                cnt=1
                can=False
        else:
            can = False
            if num==0:
                cnt=2
            elif num==1:
                cnt=3
            elif num==2:
                cnt=0
            elif num==3:
                cnt=1


    def DFS(x,y):
        global answer,cnt,can
        print(x,y,cnt)
        answer+=1
        if not (0<=x<n and 0<=y<m):
            return
        else:
            nx=x+dx[cnt]
            ny=y+dy[cnt]
            if not (0 <= nx < n and 0 <= ny < m):
                DFS(nx,ny)
            else:
                if not board[nx][ny]:
                    DFS(nx,ny)
                elif board[nx][ny]:
                    can=True
                    change(nx,ny,cnt)
                    durability[nx][ny]-=1
                    if durability[nx][ny]==0:
                        board[nx][ny]=0
                    if can:
                        DFS(nx,ny)
                    else:
                        answer-=1
                        if  board[x][y]:
                            change(x,y,cnt)
                            durability[nx][ny] -= 1
                            if durability[nx][ny] == 0:
                                board[nx][ny] = 0
                        DFS(x,y)


    n=len(board)
    m=len(board[0])
    answer=0
    cnt=0
    if not board[0][0]:
        DFS(0,0)
    return answer







if __name__ == '__main__':
    solution(		[[0, 2, 0], [0, 5, 0], [0, 0, 0]], [[0, 2, 0], [0, 1, 0], [0, 0, 0]])