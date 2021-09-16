def solution(nums):
    global number
    def go(s,n,x,y):
        global number
        if num[n]==1:
            visited[x][y]=number
            number+=1
        else:
            if not visited[x][y]:
                go(s//num[n],n+1,x,y)
            i=0
            cnt=0
            nx=x
            ny=y
            while cnt<(num[n]*num[n]-1):
                beforeX = nx
                beforeY = ny
                nx=nx+dx[i%4]*(s//num[n])
                ny=ny+dy[i%4]*(s//num[n])
                if x<=nx<x+s and y<=ny<y+s:
                    if not visited[nx][ny]:
                        go(s//num[n],n+1,nx,ny)
                        cnt+=1
                    else:
                        nx, ny = beforeX, beforeY
                        i += 1
                else:
                    nx,ny=beforeX,beforeY
                    i+=1
    number=1
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    temp=1
    for num in nums:
        temp*=num
    visited=[[0]*temp for _ in range(temp)]

    num=nums[::-1]+[1]
    go(temp,0,0,0)
    for i in visited:
        print(i)

if __name__ == '__main__':
    solution([2,4])