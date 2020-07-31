import sys
input=sys.stdin.readline
n=int(input())
def find(x):
    if parent[x]==x:
        return x
    else:
        return find(parent[x])
def merge(x,y):
    q=find(x)
    w=find(y)
    if q==w:
        print(cnt[w])
    elif q>w:
        cnt[w]+=cnt[q]
        parent[q]=w
        print(cnt[w])
    else:
        cnt[q]+=cnt[w]
        parent[w]=q
        print(cnt[q])


for _ in range(n):
    m=int(input())
    parent ={}
    cnt={}
    for _ in range(m):
        a,b=list(input().split())
        if a not in parent:
            parent[a]=a
            cnt[a]=1
        if b not in parent:
            parent[b]=b
            cnt[b]=1
        merge(a,b)