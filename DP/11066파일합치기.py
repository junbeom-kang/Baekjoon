import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    n=int(input())
    score=list(map(int,input().split()))
    sum=[0 for _ in range(n)]
    dp=[[sys.maxsize for _ in range(n)]for _ in range(n)]
    dp[0][0]=0
    sum[0]=score[0]
    for i in range(1,n):
        sum[i]=sum[i-1]+score[i]
        dp[i][i]=0
    sum.append(0)
    for d in range(1,n):
        for i in range(n-d):
            for mid in range(i,i+d):
                dp[i][i+d]=min(dp[i][i+d],dp[i][mid]+dp[mid+1][i+d]+sum[i+d]-sum[i-1])
    print(dp[0][-1])


