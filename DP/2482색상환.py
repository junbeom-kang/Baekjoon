import sys
input=sys.stdin.readline
INF=sys.maxsize
n=int(input())
k=int(input())
dp=[[-1]*(k+1) for _ in range(n)]
def DFS(n,k):
    if k==0:
        return 1
    if n<=0:
        return 0
    if dp[n][k]!=-1:
        return dp[n][k]
    dp[n][k]=0
    for i in range(n,0,-1):
        if i//2+1<k:
            break
        dp[n][k]+=DFS(i-2,k-1)
    return dp[n][k]

if k==1:
    print(n)
elif k>(n//2):
    print(0)
else:
    DFS(n-1,k)
    print((dp[n-1][k]+dp[n-3][k-1])%1000000003)