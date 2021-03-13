import sys
from heapq import *
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
temp=0
INF=sys.maxsize
def dijkstra(v):
    Temp=[INF]*n
    Temp[v]=0
    Q=[]
    heappush(Q,(0,v))
    while Q:
        weight,where=heappop(Q)
        if Temp[where]!=weight:
            continue
        else:
            for c,w in adj[where]:
                if Temp[w]>weight+c:
                    Temp[w]=weight+c
                    path[w]=[where]
                    heappush(Q,(Temp[w],w))
                elif Temp[w]==weight+c:
                    path[w].append(where)
                    heappush(Q,(Temp[w],w))
    return Temp[m]

def DFS(v):
    global ans,temp,count
    check[v]=True
    if v==0:
        ans=min(ans,temp)
    if count==cnt:
        return
    for i in path[v]:
        if not check[i]:
            temp+=arr[v][i]
            DFS(i)
            check[i]=False
            temp-=arr[v][i]

n,m=map(int,input().split())
color=[0]*n
count=0
check=[False]*n
ans=INF
adj=[[] for _ in range(n)] #경로
arr=[[] for _ in range(n)] #배열
path=[[] for _ in range(n)]
for i in range (n):
    color[i]=int(input())
for i in range(n):
    arr[i]=list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        if arr[i][j]==0:
            continue
        else:
            if color[i]==color[j]:
                adj[i].append((0,j))
                adj[j].append((0,i))
            else:
                adj[i].append((1, j))
                adj[j].append((1, i))
print(arr)
print(adj)
cnt=dijkstra(0)
DFS(m)
print(cnt,ans)


