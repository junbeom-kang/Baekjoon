import sys
sys.setrecursionlimit(10**6)
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
input=sys.stdin.readline
N,Q=map(int,input().split())
parent=[i for i in range(N+1)]
mom=[0]*(N+1)
for i in range(2,N+1):
    mom[i]=int(input())
temp=[]
ans=[]
for i in range(N+Q-1):
    temp.append(list(map(int,input().split())))
for i in temp[::-1]:
    if i[0]==1:
        if find(i[1])==find(i[2]):
            ans.append('YES')
        else:
            ans.append('NO')
    else:
        #merge(i[1],mom[i[1]])
        parent[i[1]]=mom[i[1]]
for i in ans[::-1]:
    print(i)