import sys
input=sys.stdin.readline


def bfs():
    Q=[(0,0,False)]
    ans = 1
    while Q:
        Q2=[]
        for a,b,c in Q:
            if a==n-1 and b==m-1:
                return ans
            for i,j in dir:
                rx=a+i
                ry=b+j
                if 0<=rx<n and 0<=ry<m:
                    if not c:
                        if not check1[rx][ry]:
                            if stack[rx][ry]=='0':
                                check1[rx][ry]=True
                                Q2.append((rx,ry,False))
                            else:
                                check1[rx][ry]=True
                                Q2.append((rx,ry,True))
                    else:
                        if not check[rx][ry]:
                            if stack[rx][ry]=='0':
                                check[rx][ry]=True
                                Q2.append((rx,ry,True))
        Q=Q2
        ans+=1
    return -1


n,m=list(map(int,input().split()))
stack=[list(input())for _ in range(n)]
check=[[False]*m for _ in range(n)]
check1=[[False]*m for _ in range(n)]
dir=[[1,0],[-1,0],[0,1],[0,-1]]

print(bfs())





