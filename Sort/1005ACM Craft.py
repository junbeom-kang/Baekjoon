import sys
from collections import deque
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    n,k=map(int,input().split())
    Q=deque([])
    adj=[[] for _ in range(n+1)]
    degree=[0]*(n+1)
    dp=[-1]*(n+1)
    cost=list(map(int,input().split()))
    from_where=[[]for _ in range(n+1)]
    order=[]
    for i in range(k):
        a,b=map(int,input().split())
        adj[a].append(b)
        from_where[b].append(a)
        degree[b]+=1
    ans=int(input())
    for i in range(1,n+1):
        if degree[i]==0:
            Q.append(i)

    for i in range(n):
        temp=Q.popleft()
        order.append(temp)
        for j in adj[temp]:
            degree[j]-=1
            if degree[j]==0:
                Q.append(j)
    for i in order:
        temp=-1
        if len(from_where[i])==0:
            dp[i]=cost[i-1]
        else:
            for j in from_where[i]:
                temp=max(temp,dp[j])
                dp[i]=temp+cost[i-1]
    print(dp[ans])