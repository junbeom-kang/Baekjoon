import sys
#N이 1일때 생각해야됨.
INF=sys.maxsize
input=sys.stdin.readline
n=int(input())
if n==1:
    p,q=map(int,input().split())
    print(min(p,q))
else:
    dp=[[0]*(n+1) for _ in range(2)]
    arr=[[0]*(n+1) for _ in range(2)]
    change=[[0]*(n+1) for _ in range(2)]
    for i in range(1,n):
        a,b,c,d=map(int,input().split())
        arr[0][i]=a
        arr[1][i]=b
        change[0][i+1]=c #a에서 b가 0번인덱스
        change[1][i+1]=d
    arr[0][n],arr[1][n]=map(int,input().split())
    dp[0][1]=arr[0][1]
    dp[1][1]=arr[1][1]
    for i in range(2,n+1):
        dp[0][i]=min(dp[0][i-1]+arr[0][i],dp[1][i-1]+arr[0][i]+change[1][i])
        dp[1][i]=min(dp[1][i-1]+arr[1][i],dp[0][i-1]+arr[1][i]+change[0][i])
    print(min(dp[0][n],dp[1][n]))
