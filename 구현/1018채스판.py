import sys
n,m=map(int,input().split())
def color(a,b,c,d):
    cnt1=0
    k=1
    for i in range(a,a+8):
        for j in range(b,b+8):
            if k>0:
                if adj[i][j]==c:
                    cnt1+=1
            elif k<0:
                if adj[i][j]==d:
                    cnt1+=1
            k*=-1
        k*=-1
    return cnt1

adj=[list(input().rstrip())for _ in range(n)]
temp=sys.maxsize
for i in range(n-7):
    for j in range(m-7):
        temp=min(temp,min(color(i,j,'B','W'),color(i,j,'W','B')))
print(temp)
