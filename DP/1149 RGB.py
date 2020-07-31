import sys
input=sys.stdin.readline
minvalue=float('INF')
n=int(input())
sum=[[minvalue for _ in range(3)]for _ in range(n)]
adj=[list(map(int,input().split()))for _ in range(n)]
sum[0]=adj[0]
for i in range(1,n):
    for j in range(3):
        if j==0:
            sum[i][j]=min(sum[i-1][1],sum[i-1][2])+adj[i][j]
        elif j==1:
            sum[i][j]=min(sum[i-1][0],sum[i-1][2])+adj[i][j]
        else:
            sum[i][j]=min(sum[i-1][1],sum[i-1][0])+adj[i][j]
print(min(sum[n-1]))

