import sys
input=sys.stdin.readline
N,M,D=map(int,input().split())
min_val=float('-inf')
adj=[[]for _ in range(N)]
sum=[[min_val for _ in range(M)]for _ in range(N)]
sum[0]=[0 for _ in range(M)]
for i in range(N):
    adj[i].extend(map(int,input().split()))
def DP(i,j,d):
    dec=j
    inc=j+1
    for k in range(i-d,i):
        for m in range(dec,inc):
            if 0<=k<=N-1 and 0<=m<=M-1:
                sum[i][j]=max(sum[i][j],sum[k][m]+adj[i][j]*adj[k][m])
        dec-=1
        inc+=1

for i in range(1,N):
    for j in range(0,M):
        DP(i,j,D)
print(max(sum[N-1]))
