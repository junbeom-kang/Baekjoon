import sys
input=sys.stdin.readline
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
            cnt[q]+=cnt[w]
        else:
            parent[q]=w
            cnt[w]+=cnt[q]
def sinbal(a,b,c):
    return (a[0]*b[1]+b[0]*c[1]+c[0]*a[1])-(a[1]*b[0]+b[1]*c[0]+c[1]*a[0])
def ccw(a,b):
    fx=a[0:2]
    fy=a[2:]
    sx=b[0:2]
    sy=b[2:]
    first=sinbal(fx,fy,sx)*sinbal(fx,fy,sy)
    second=sinbal(sx,sy,fx)*sinbal(sx,sy,fy)
    if first==0 and second==0:
        if fx>fy:
            fx,fy=fy,fx
        if sx>sy:
            sx,sy=sy,sx
        if fx<=sy and sx<=fy:
            return True
        else:
            return False
    else:
        if first<=0 and second<=0:
            return True
        else:
            return False

n=int(input())
adj=[]
for i in range(n):
    adj.append(list(map(int,input().split())))
cnt=[1]*n
parent=[i for i in range(n)]
for i in range(n-1):
    for j in range(i+1,n):
        if ccw(adj[i],adj[j]):
            merge(i,j)
ans=[]
for i in range(n):
    ans.append(find(i))
print(len(set(ans)))
print(max(cnt))
