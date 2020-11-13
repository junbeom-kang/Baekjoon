import sys
from collections import deque
input=sys.stdin.readline
def go(r,rr,b,bb,c,d):
    tmp=r
    tmp1=rr
    tmp2=b
    tmp3=bb
    can=False
    if c==1:
        if (rr>bb and d==-1) or (rr<bb and d==1):
            while adj[b][bb+d]!='#' and not(b==r and bb+d==rr):
                bb+=d
                if adj[b][bb]=='O':
                    return 0
            while adj[r][rr+d]!='#' and not(r==b and rr+d==bb):
                rr+=d
                if adj[r][rr] == 'O':
                    return 1
            if tmp==r and tmp1==rr and tmp2==b and tmp3==bb:
                return 0
            return ((r,rr),(b,bb))
        else:
            while adj[r][rr+d]!='#' and not(b==r and rr+d==bb):
                rr+=d
                if adj[r][rr]=='O':
                    r,rr=-1,-1
                    can=True
                    break

            while adj[b][bb+d]!='#' and not(r==b and bb+d==rr):
                bb+=d
                if adj[b][bb] == 'O':
                    return 0
            if can:
                return 1
            else:
                if tmp==r and tmp1==rr and tmp2==b and tmp3==bb:
                    return 0
                return ((r,rr),(b,bb))
    else:
        if (r>b and d==-1) or (r<b and d==1):
            while adj[b+d][bb]!='#' and not(b+d==r and bb==rr):
                b+=d
                if adj[b][bb]=='O':
                    return 0
            while adj[r+d][rr]!='#' and not(rr==bb and r+d==b):
                r+=d
                if adj[r][rr] == 'O':
                    return 1
            if tmp==r and tmp1==rr and tmp2==b and tmp3==bb:
                return 0
            return ((r,rr),(b,bb))
        else:
            while adj[r+d][rr]!='#' and not(r+d==b and bb==rr):
                r+=d
                if adj[r][rr]=='O':
                    r,rr=-1,-1
                    can=True
                    break
            while adj[b+d][bb]!='#' and not(rr==bb and b+d==r):
                b+=d
                if adj[b][bb] == 'O':
                    return 0
            if can:
                return 1
            else:
                if tmp==r and tmp1==rr and tmp2==b and tmp3==bb:
                    return 0
                return ((r,rr),(b,bb))


def BFS(R,B):
    cnt=1
    Q=deque([(R,B)])
    while Q:
        for i in range(len(Q)):
            o,p=Q.popleft()
            for k in range(2):
                for e in range(-1,2,2):
                    q=go(o[0],o[1],p[0],p[1],k,e)
                    if q:
                        if q==1:
                            return cnt
                        else:
                            Q.append(q)

        cnt+=1
        if cnt>10:
            return -1
    return -1

n,m=map(int,input().split())
adj=[list(input().rstrip())for _ in range(n)]

for i in range(n):
    for j in range(m):
        if adj[i][j]=='R':
            R=[i,j]
        elif adj[i][j]=='B':
            B=[i,j]
        elif adj[i][j]=='O':
            E=[i,j]
print(BFS(R,B))

