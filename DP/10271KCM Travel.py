import sys
input=sys.stdin.readline
INF=sys.maxsize
T=int(input())
for _ in range(T):
    n,m,k=map(int,input().split())
    dp=[[INF]*(m+1)for _ in range(n+1)]
    adj=[[]for _ in range(n+1)]
    for _ in range(k):
        a,b,c,d=map(int,input().split())
        adj[a].append((b,c,d))

    dp[1][0]=0
    for i in range(m+1):
        for j in range(1,n+1):
            if dp[j][i]==INF:
                continue
            for b,c,d in adj[j]:
                if i+c>m:
                    continue
                dp[b][i+c]=min(dp[j][i]+d,dp[b][i+c])
    ans=min(dp[n])
    if ans==INF:
        print('Poor KCM')
    else:
        print(ans)