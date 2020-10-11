import sys
import copy
from itertools import combinations
input=sys.stdin.readline
n,m=map(int,input().split())
def DFS(x,y):
    for t in range(4):
        rx = x + dx[t]
        ry = y + dy[t]
        if 0 <= rx < n and 0 <= ry < m:
            if temp[rx][ry] == 0:
                temp[rx][ry]=2
                DFS(rx, ry)

dx=[0,0,1,-1]
dy=[1,-1,0,0]
virus=[]
zero=[]
adj=[[] for _ in range(n)]
for i in range(n):
    adj[i]=list(map(int,input().split()))
for i in range(n):
    for j in range(m):
        if adj[i][j]==2:
            virus.append((i,j))
        elif adj[i][j]==0:
            zero.append((i,j))
ans1=0
for i in combinations(zero,3):
    cnt1=0
    temp=copy.deepcopy(adj)
    for j in i:
        temp[j[0]][j[1]]=1
    for x,y in virus:
        DFS(x,y)
    for k in range(n):
        for t in range(m):
            if temp[k][t]==0:
                cnt1+=1
    ans1=max(ans1,cnt1)
print(ans1)




