import sys
from heapq import *
input=sys.stdin.readline
INF=sys.maxsize
def dijkstra(s):
    ans=[INF]*(v+1)
    ans[s]=0
    Q=[]
    heappush(Q,(0,s))
    while Q:
        a,b=heappop(Q)
        if a>ans[b]:
            continue
        else:
            for q,w in adj[b]:
                if ans[b]+w<ans[q]:
                    ans[q]=ans[b]+w
                    heappush(Q,(ans[q],q))
    return ans

v,e,p=map(int,input().split())
adj=[[]for _ in range(v+1)]
for _ in range(e):
    a,b,c=map(int,input().split())
    adj[a].append((b,c))
    adj[b].append((a,c))
temp=dijkstra(1)
where=dijkstra(p)
if temp[p]+where[v]==temp[v]:
    print('SAVE HIM')
else:
    print('GOOD BYE')