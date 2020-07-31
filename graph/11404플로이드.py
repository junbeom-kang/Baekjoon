import sys,copy
def input():
    return sys.stdin.readline()

n=int(input())
m=int(input())
arr=[[1000000]*(n+1) for _ in range(n+1)]
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
            if arr[i][k]+arr[k][j]<arr[i][j]:
                arr[i][j]=arr[i][k]+arr[k][j]
for i in range(1,n+1):
    for j in range(1,n+1):
        if arr[i][j]==1000000:
            print(0,end=' ')
            continue
        print(arr[i][j],end=' ')
    print()