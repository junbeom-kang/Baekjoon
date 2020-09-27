import sys
from collections import deque
T=int(input())
for _ in range(T):
    input=sys.stdin.readline
    n=int(input())
    adj=[[]for _ in range(n+1)]
    degree=[0]*(n+1)
    data=list(map(int,input().split()))
    for i in range(len(data)-1):
        for j in range(i+1,len(data)):
            adj[data[i]].append(data[j])
            degree[data[j]]+=1
    m=int(input())
    for _ in range(m):
        a,b=map(int,input().split())
        if  a in adj[b]:
            adj[b].remove(a)
            degree[a] -= 1
            adj[a].append(b)
            degree[b]+=1
        else:
            adj[a].remove(b)
            degree[b]-=1
            adj[b].append(a)
            degree[a]+=1
    Q=deque([])
    ans=[]
    for i in range(1,n+1):
        if degree[i]==0:
            Q.append(i)
    can=True
    for i in range(1,n+1):
        if len(Q)>1:
            print('?')
            can=False
            break
        elif not Q:
            print('IMPOSSIBLE')
            can=False
            break
        else:
            temp=Q.popleft()
            ans.append(temp)
            for j in adj[temp]:
               degree[j]-=1
               if degree[j]==0:
                   Q.append(j)
    if can:
        print(*ans)
