#지역변수와 for문 등등의 변수를 너무 혼동되게써서 코드를 고치는데도 애먹고
#코드짜기도 힘들었다 변수를 확실히 정하자 사람들이 _를써서 변수를 정하는 이유를 알겟다.

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
def dfs(cnt,C):
    global ans
    if cnt==len(C):
        temp=0
        for k in range(n):
            for l in range(m):
                if adj[k][l]==0:
                    temp+=1
        ans=min(ans,temp)
    else:
        i=C[cnt][0]
        j=C[cnt][1]
        k=C[cnt][2]
        if k==1:
            for q in range(4):
                T=CCTV(i,j,[q])
                dfs(cnt+1,C)
                for _ in range(T):
                    r1,r2=back.pop()
                    adj[r1][r2]=0
        elif k==3:
            for q in range(4):
                T=CCTV(i,j,[q,(q+1)%4])
                dfs(cnt + 1, C)
                for _ in range(T):
                    r1, r2 = back.pop()
                    adj[r1][r2] = 0
        elif k==2:
            for q in range(2):
                T=CCTV(i,j,[q,q+2])
                dfs(cnt + 1, C)
                for _ in range(T):
                    r1, r2 = back.pop()
                    adj[r1][r2] = 0
        elif k==4:
            for q in range(4):
                T=CCTV(i,j,[q,(q+1)%4,(q+2)%4])
                dfs(cnt + 1, C)
                for _ in range(T):
                    r1, r2 = back.pop()
                    adj[r1][r2] = 0
        elif k==5:
            T=CCTV(i,j,[0,1,2,3])
            dfs(cnt + 1, C)
            for _ in range(T):
                r1, r2 = back.pop()
                adj[r1][r2] = 0


def CCTV(i,j,W):
    time=0
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    for w in W:
        a=i+dx[w]
        b=j+dy[w]
        while 0<=a<n and 0<=b<m and adj[a][b]!=6:
            if adj[a][b]==0:
                back.append((a,b))
                adj[a][b]=-1
                time+=1
            a+=dx[w]
            b+=dy[w]
    return time


def solution(adj):
    C=[]
    for i in range(n):
        for j in range(m):
            if 1<=adj[i][j]<=5:
                C.append((i,j,adj[i][j]))
    dfs(0,C)
    return ans

back=[]
n,m=map(int,input().split())
adj=[list(map(int,input().split())) for _ in range(n)]
ans = 100
print(solution(adj))