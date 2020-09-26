from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
adj=[[]for _ in range(n+1)]
degree=[0]*(n+1)
Q=deque([])
ans=[]
can=True
for _ in range(m):
    temp=list(map(int,input().split()))
    for i in range(1,temp[0]):
        adj[temp[i]].append(temp[i+1])
        degree[temp[i+1]]+=1
for i in range(1,n+1):
    if degree[i]==0:
        Q.append(i)
for i in range(n):
    if not Q:
        can=False
        break
    else:
        temp=Q.popleft()
        ans.append(temp)
        for i in adj[temp]:
            degree[i]-=1
            if degree[i]==0:
                Q.append(i)
if can:
    for _ in ans:
        print(_)
else:
    print(0)
