from collections import deque
import sys
input=sys.stdin.readline
ans=[]
n,m=map(int,input().split())
Q=deque([])
degree=[0]*(n+1)
adj=[[]for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    adj[a].append(b)
    degree[b]+=1

for i in range(1,n+1):
    if degree[i]==0:
        Q.append(i)
for i in range(n):
    temp=Q.popleft()
    ans.append(temp)
    for j in adj[temp]:
        degree[j]-=1
        if degree[j]==0:
            Q.append(j)
print(*ans)
