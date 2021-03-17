import sys
#N이 1일때 생각해야됨.
INF=sys.maxsize
input=sys.stdin.readline
n,m=map(int,input().split())
if n==1:
    p,q=map(int,input().split())
    print(min(p,q))
else:
    dp=[[INF]*(n+1) for _ in range(n+1)]
    arr=[[0]*(n+1) for _ in range(n+1)]
    change=[[0]*(n+1) for _ in range(n+1)]
    for i in range(1,m):
        temp=list(map(int,input().split()))
        for j in range(1,n+1):
            arr[j][i]=temp[j-1]
        for j in range(1,n+1):
            change[j][i+1]=temp[j+n-1]
    for i in range(1,n+1):
        dp[i][1]=arr[i][1]
    for i in range(2,m+1):
        for j in range(1,n+1):
            if i==j:
                t=arr[j][i]+dp[j][i-1]
            else:
                t=arr[j][i]+dp[i-1][j]+change[i][j]
            dp[i][j]=min(dp[i][j],t)
    ans=INF
    for i in range(1,n+1):
        ans=min(ans,dp[i][m-1])
    print(ans)