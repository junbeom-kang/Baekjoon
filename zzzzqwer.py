import sys
from itertools import combinations
input=sys.stdin.readline
n,m=map(int,input().split())
def DFS(r,c):
    if r>n or c>m:
        return
    if temp[r][c + 1] == 0:
        temp[r][c + 1] = 2
        DFS(r, c + 1)
    if temp[r + 1][c] == 0:
        temp[r + 1][c] = 2
        DFS(r + 1, c)

    if temp[r - 1][c] == 0:
        temp[r - 1][c] = 2
        DFS(r - 1, c)

    if temp[r][c - 1] == 0:
        temp[r][c - 1] = 2
        DFS(r, c - 1)


dx=[0,0,1,-1]
dy=[1,-1,0,0]
virus=[]
zero=[]
adj=[[1,1,1,1,1,1,1,1,1,1]]
for i in range(n):
    adj.append([1]+list(map(int,input().split()))+[1])
adj+=[[1,1,1,1,1,1,1,1,1,1]]
for i in range(n+2):
    for j in range(m+2):
        if adj[i][j]==2:
            virus.append((i,j))
        elif adj[i][j]==0:
            zero.append((i,j))
ans1=0
for i in combinations(zero,3):
    cnt1=0
    temp=[[]for _ in range(n+2)]
    #각 리스트를 shallow copy
    for row in range(n+2):
        temp[row]=adj[row][:]
    for j in i:
        temp[j[0]][j[1]]=1
    for x,y in virus:
        DFS(x,y)
    for k in range(n+2):
        cnt1+=temp[k].count(0)
    ans1=max(ans1,cnt1)
print(ans1)
