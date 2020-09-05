import sys
sys.setrecursionlimit(10**9)
def DFS(v):
    visit[v]=1
    leaf=True
    for i in adj[v]:
        if visit[i]==-1:
            DFS(i)
            dp[v][1]+=dp[i][0]
            dp[v][0]+=max(dp[i][1],dp[i][0])
            leaf=False
    if leaf:
        dp[v][1]=w[v-1]
        dp[v][0]=0
    else:
        dp[v][1]+=w[v-1]
def tracking(v,pre):
    visit[v]=1
    if pre==0:
        if dp[v][1]>dp[v][0]:
            A.append(v)
            for i in adj[v]:
                if visit[i]==-1:
                    tracking(i,1)
        else:
            for i in adj[v]:
                if visit[i]==-1:
                    tracking(i,0)
    else:
        for i in adj[v]:
            if visit[i]==-1:
                tracking(i,0)


input=sys.stdin.readline
n=int(input())
w=list(map(int,input().split()))
dp=[[0 for _ in range(2)]for _ in range(n+1)]
visit=[-1]*(n+1)
A=[]
adj=[[]for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
DFS(1)
visit=[-1]*(n+1)
tracking(1,0)
A.sort()
ans=max(dp[1])
print(ans)
print(*A)