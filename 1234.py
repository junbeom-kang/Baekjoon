import sys
from heapq import *
sys.setrecursionlimit(10**9)
INF=sys.maxsize
input=sys.stdin.readline
def dijkstra(s):
    ans=[INF]*n
    ans[s]=0
    Q=[]
    heappush(Q,(0,s))
    while Q:
        a,b=heappop(Q)
        if ans[b]<a:
            continue
        else:
            for q in adj[b]:
                w=adj[b][q]
                if ans[q]>ans[b]+w:
                    ans[q]=ans[b]+w
                    heappush(Q,(ans[q],q))
    return ans

def tracking(ans,last):
    global delete
    temp=ans[last]
    for i in where[last]:
        if ans[i]>ans[last]:
            continue
        elif ans[i]+adj[i][last]==temp:
            if (i,last) not in delete:
                delete.add((i,last))
                tracking(ans,i)

while 1:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    s,d=map(int,input().split())
    adj=[{}for _ in range(n)]
    where=[[]for _ in range(n)]
    delete=set()
    for i in range(m):
        a,b,c=map(int,input().split())
        adj[a][b]=c
        where[b].append(a)
    ans=dijkstra((s))
    tracking(ans,d)
    for a,b in delete:
        del adj[a][b]
    temp=dijkstra(s)[d]
    if temp==INF:
        print(-1)
    else:
        print(temp)