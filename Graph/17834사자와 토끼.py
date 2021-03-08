import sys
import math
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v,c):
    check[v]=True
    color[v]=c
    for i in arr[v]:
        if check[i]:
            if color[i]==c:
                print('0')
                sys.exit()
        else:
            dfs(i,c*-1)



n,m=map(int,input().split())
check=[False]*(n+1)
color=[0]*(n+1)
arr=[[]for _ in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

dfs(1,1)
cnt=0
for i in color:
    if i==1:
        cnt+=1
print(cnt*(n-cnt)*2)
