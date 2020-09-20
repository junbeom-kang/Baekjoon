import sys
input=sys.stdin.readline
def CCTV(i,j,W):
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    back=[]
    for w in W:
        a=i+dx[w]
        b=j+dy[w]
        while 0<=a<n and 0<=b<m and adj[a][b]!=6:
            if adj[a][b]==0:
                back.append((a,b))
                adj[a][b]=-1
            a+=dx[w]
            b+=dy[w]
    print(adj)
    return back

def dfs(cnt,C):
    global ans,m,n
    if cnt==len(C):
        temp=0
        print(adj)
        for k in range(n):
            for l in range(m):
                if adj[k][l]==0:
                    print(k,l,'!!!!!')
                    temp+=1
        ans=min(ans,temp)
    else:
        i=C[cnt][0]
        j=C[cnt][1]
        k=C[cnt][2]
        print(i,j,k)
        if k==1:
            for m in range(4):
                temp=CCTV(i,j,[m])
                dfs(cnt+1,C)
                print(adj)
                for i in temp:
                    adj[i[0]][i[1]]=0
                    print(adj,'!')
        elif k==3:
            for m in range(4):
                temp=CCTV(i,j,[m,(m+1)%4])
                dfs(cnt + 1, C)
                for i in temp:
                    adj[i[0]][i[1]] = 0
        elif k==2:
            for m in range(2):
                temp=CCTV(i,j,[i,i+2])
                dfs(cnt + 1, C)
                for i in temp:
                    adj[i[0]][i[1]] = 0
        elif k==4:
            for m in range(4):
                temp=CCTV(i,j,[m,(m+1)%4,(m+2)%4])
                dfs(cnt + 1, C)
                for i in temp:
                    adj[i[0]][i[1]] = 0
        elif k==5:
            temp=CCTV(i,j,[0,1,2,3])
            dfs(cnt + 1, C)
            for i in temp:
                adj[i[0]][i[1]] = 0




def solution(adj):
    C=[]
    for i in range(n):
        for j in range(m):
            if 1<=adj[i][j]<=5:
                C.append((i,j,adj[i][j]))
    dfs(0,C)
    return ans

n,m=map(int,input().split())
adj=[list(map(int,input().split())) for _ in range(n)]
ans = 100
print(solution(adj))