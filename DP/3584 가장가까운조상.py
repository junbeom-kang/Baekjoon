import sys
import math
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
def DFS(v,d):
    check[v]=True
    depth[v]=d
    for i in child[v]:
        if check[i]:
            continue
        else:
            dp[0][i]=v
            DFS(i,d+1)
T=int(input())
for i in range(T):
    n=int(input())
    logn=int(math.ceil(math.log2(n)))
    dp=[[0]*(n+1) for _ in range(logn+1)]
    child=[[]for _ in range(n+1)]
    parent = [[]for _ in range(n+1)]
    for i in range(n-1):
        a,b=map(int,input().split())
        child[a].append(b)
        parent[b].append(a)
    depth=[0]*(n+1)
    check=[False]*(n+1)
    v=1
    while parent[v]:
        v=parent[v][0]
    DFS(v,0)
    for i in range(1,logn+1):
        for j in range(1,n+1):
            dp[i][j]=dp[i-1][dp[i-1][j]]
    a, b = map(int, input().split())
    if depth[a] >= depth[b]:
        a, b = b, a  # b가 깊어짐
    for i in range(logn, -1, -1):
        if depth[b] - depth[a] >= 1 << i:
            b = dp[i][b]
    if a == b:
        print(a)
        continue
    for i in range(logn, -1, -1):
        if dp[i][a] != dp[i][b]:
            a = dp[i][a]
            b = dp[i][b]
    print(dp[i][a])

