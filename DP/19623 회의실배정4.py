import sys
import bisect
input=sys.stdin.readline
n=int(input())
adj=[]
B=[]
for _ in range(n):
    a,b,c=map(int,input().split())
    adj.append((a,b,c))
    B.append(b)
adj.sort(key=lambda x:x[1])
B.sort()
dp=[0]*n
dp[0]=adj[0][2]
for i in range(1,n):
    temp=adj[i][0]
    BS=bisect.bisect(B,temp)
    if BS==0:
        dp[i]=max(dp[i-1],adj[i][2])
    else:
        dp[i]=max(dp[i-1],dp[BS-1]+adj[i][2])
print(dp[n-1])