import sys
input=sys.stdin.readline
n=int(input())
data=list(map(int,input().split()))
m=int(input())
dp=[[[]for _ in range(n+1)]for _ in range(n+1)]
for d in range(n):
    for i in range(1,n-d+1):
        if d==0:
            dp[i][i]=1
        elif d==1:
            if data[i-1]==data[i+d-1]:
                dp[i][i+d]=1
            else:
                dp[i][i+d]=0
        else:
            if dp[i+1][i+d-1]==1:
                if data[i-1]==data[i+d-1]:
                    dp[i][i+d]=1
                else:
                    dp[i][i+d]=0
            else:
                dp[i][i+d]=0
for i in range(m):
    a,b=map(int,input().split())
    print(dp[a][b])
