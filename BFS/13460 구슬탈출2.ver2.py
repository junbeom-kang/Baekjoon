import sys
from collections import deque
input=sys.stdin.readline
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def go(x,y,wx,wy):
    fc=False
    sc=False
    for t,i in enumerate([x,y]):
        while adj[i[0]+wx][i[1]+wy]!='#' and (i[0]+wx,i[1]+wy)!=(x[0],x[1]):
            if adj[i[0]+wx][i[1]+wy]=='O':
                if t==0:
                    x[0]=-1
                    x[1]=-1
                    fc=True
                else:
                    sc=True
            i[0]+=wx
            i[1]+=wy
    return x,y,fc,sc
def slide(r,b,d):
    qqq=False
    www=False
    if d==0:
        if r[1]>b[1]:
            x,y,fc,sc=go(r,b,dx[d],dy[d])
        else:
            y,x,sc,fc,=go(b,r,dx[d],dy[d])
    elif d==1:
        if r[1]<b[1]:
            x, y, fc, sc = go(r, b, dx[d], dy[d])

        else:
            y,x,sc,fc,=go(b,r,dx[d],dy[d])
    elif d==2:
        if r[0]<b[0]:
            x, y, fc, sc = go(r, b, dx[d], dy[d])

        else:
            y,x,sc,fc,=go(b,r,dx[d],dy[d])
    else:
        if r[0]>b[0]:
            x, y, fc, sc = go(r, b, dx[d], dy[d])

        else:
            y,x,sc,fc,=go(b,r,dx[d],dy[d])
    if fc==True and sc==False:
        qqq=True
    if fc==False and sc==False:
        www=True
    return qqq,www,x,y

def bfs(R,B):
    Q=deque([[R,B]])
    cnt=1
    while Q:
        for _ in range(len(Q)):
            c,v=Q.popleft()
            for d in range(4):
                r,b=c[:],v[:]
                goal,can,nr,nb=slide(r,b,d)
                if goal:
                    return cnt
                if can and (nr!=c or nb!=v):
                    Q.append([nr,nb])
        cnt+=1
        if cnt>10:
            return -1
    return -1

n,m=map(int,input().split())
adj=[list(input().rstrip()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if adj[i][j]=='#'or adj[i][j]==',':
            continue
        if adj[i][j]=='O':
            end=[i,j]
        elif adj[i][j]=='R':
            R=[i,j]
        elif adj[i][j]=='B':
            B=[i,j]
print(bfs(R,B))
