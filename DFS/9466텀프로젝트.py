import sys
sys.setrecursionlimit(10**8)
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    n=int(input())
    data=[0]+list(map(int,input().split()))
    visited=[0]*(n+1)
    ans=0
    for i in range(1,n+1):
        if not visited[i]:
            v=i
            while not visited[v]:
                 visited[v]=1
                 v=data[v]
            w=i
            while w!=v:
                ans+=1
                w=data[w]
    print(ans)


