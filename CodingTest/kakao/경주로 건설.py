import sys
dx=[0,-1,0,1]
dy=[1,0,-1,0]
ans=sys.maxsize

def solution(board):
    n=len(board)
    dp=[[[sys.maxsize]*4 for _ in range(n)]for _ in range(n)]
    check=[[False]*n for _ in range(n)]
    check[0][0]=True
    if board[0][1]!=1:
        check[0][1]=True
        dp[0][1][0]=100
        DFS(0,1,n,check,100,board,0,dp)
        check[0][1]=False
    if board[1][0]!=1:
        check[1][0]=True
        dp[1][0][3] = 100
        DFS(1,0,n,check,100,board,3,dp)
        check[1][0]=False
    answer = ans
    return answer


def DFS(x,y,n,check,sum,board,way,dp):
    global ans
    if x==n-1 and y==n-1:
        if sum<ans:
            ans=sum
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if n-1<nx or 0>nx or n-1<ny or 0>ny:
            continue
        if check[nx][ny] or board[nx][ny]==1:
            continue
        if i%2==way%2:
            if dp[nx][ny][i]>=sum+100:
                check[nx][ny] = True
                dp[nx][ny][i]=sum+100
                DFS(nx,ny,n,check,sum+100,board,i,dp)
                check[nx][ny] = False
        else:
            if dp[nx][ny][i]>=sum+500:
                check[nx][ny] = True
                dp[nx][ny][i]=sum+500
                DFS(nx,ny,n,check,sum+600,board,i,dp)
                check[nx][ny] = False

if __name__ == '__main__':
    print(solution([[0,0,0],[0,0,0],[0,0,0]]))