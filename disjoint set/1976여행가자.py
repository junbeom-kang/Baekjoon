import sys
input=sys.stdin.readline
n=int(input())
_=int(input())
adj=[list(map(int,input().split()))for _ in range(n)]
parent=[]
for i in range(n):
    parent.append(i)
def find(v):
    if parent[v]==v:
        return v
    else:
        parent[v]=find(parent[v])
        return parent[v]
def merge(a,b):
    q=find(a)
    w=find(b)
    if q==w:
        return
    else:
        if q<=w:
            parent[w]=q
        else:
            parent[q]=w

for i in range(n):
    for j in range(i+1,n):
        if adj[i][j]==1:
            merge(i,j)
ans=list(map(int,input().split()))
temp=find(ans[0]-1)
for i in ans[1:]:
    if find(i-1)!=temp:
        print('NO')
        sys.exit()
print('YES')