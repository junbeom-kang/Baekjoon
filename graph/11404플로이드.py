import sys
input=sys.stdin.readline
INF=sys.maxsize
n=int(input())
m=int(input())
arr=[[INF]*(n+1) for _ in range(n+1)]
for i in range(m):
    x,y,z=list(map(int,input().split()))
    if z<arr[x][y]:
        arr[x][y]=z

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                arr[i][j]==0
                continue
            arr[i][j]=min(arr[i][k]+arr[k][j],arr[i][j])
for i in range(1,n+1):
    for j in range(1,n+1):
        if arr[i][j]==INF:
            print(0,end=' ')
        else:
            print(arr[i][j],end=' ')
    print()