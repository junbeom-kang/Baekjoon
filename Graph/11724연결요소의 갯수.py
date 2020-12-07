import sys
input=sys.stdin.readline
n,m=map(int,input().split())
parent=[i for i in range(n+1)]
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
        if q<w:
            parent[w]=q
        else:
            parent[q]=w
for i in range(m):
    o,p=map(int,input().split())
    merge(o,p)
for i in range(1,n+1):
    find(i)
print(len(set(parent))-1)