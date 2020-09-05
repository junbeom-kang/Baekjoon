import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
def makeTree(v):
    temp=0
    visit[v] = True
    for i in adj[v]:
        if not visit[i]:
            parent[i]=v
            temp+=makeTree(i)
    cnt[v]=temp+1
    return temp+1

n,r,q=map(int,input().split())
parent=[i for i in range(n+1)]
visit=[False]*(n+1)
cnt=[0]*(n+1)
adj=[[]for _ in range(n+1)]
for _ in range(n-1):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
makeTree(r)
for _ in range(q):
    print(cnt[int(input())])