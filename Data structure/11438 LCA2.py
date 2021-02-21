import sys
import math
from collections import deque
input=sys.stdin.readline

n=int(input())
logn=int(math.ceil(math.log2(n)))
dp=[[0]*(n+1) for _ in range(logn+1)]
tree=[[]for _ in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
depth=[0]*(n+1)
check=[False]*(n+1)
Q=deque([1])
while Q:
    temp=Q.popleft()
    check[temp]=True
    for i in tree[temp]:
        if not check[i]:
            depth[i]=depth[temp]+1
            dp[0][i]=temp
            Q.append(i)


for i in range(1,logn+1):
    for j in range(1,n+1):
        dp[i][j]=dp[i-1][dp[i-1][j]]

m=int(input())
for i in range(m):
    a,b=map(int,input().split())
    if depth[a]>=depth[b]:
        a,b=b,a     #b가 깊어짐
    for i in range(logn,-1,-1):
        if depth[b]-depth[a]>=1<<i:
            b=dp[i][b]
    if a==b:
        print(a)
        continue
    for i in range(logn,-1,-1):
        if dp[i][a]!=dp[i][b]:
            a=dp[i][a]
            b=dp[i][b]
    print(dp[i][a])