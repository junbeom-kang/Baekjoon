import sys
input=sys.stdin.readline
count=0
n=int(input())
block=list(map(int,input().split()))
temp=int(input())
adj=[[]for _ in range(n)]
for i in range(n):
    if block[i]==-1:
        start=i
    else:
        adj[block[i]].append(i)

for i in adj:
    if temp in i:
        i.remove(temp)

def dfs(v):
    global count
    if not adj[v]:
        count+=1
    else:
        for i in adj[v]:
            dfs(i)
if start==temp:
    print('0')
else:
    dfs(start)
    print(count)