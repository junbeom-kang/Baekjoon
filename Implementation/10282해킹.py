from heapq import heappush,heappop
import sys
input=sys.stdin.readline

t=int(input())
for __ in range(t):
    n,d,c=map(int,input().split())
    arr=[[] for _ in range(n+1)]
    visited=[False]*(n+1)
    for _ in range(d):
        a,b,s=map(int,input().split())
        arr[b].append([s,a])
    q=[]
    heappush(q,[0,c])
    visited[c]=True
    temp=-1
    cnt=0
    while q:
        w,d=heappop(q)
        if visited[d] and d!=c:
            continue
        temp=w
        cnt+=1
        visited[d]=True
        for s in arr[d]:
            if not visited[s[1]]:
                heappush(q,[s[0]+w,s[1]])
    print(cnt,temp)