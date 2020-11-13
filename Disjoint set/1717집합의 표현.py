import sys
input=sys.stdin.readline
n,m=map(int,input().split())
parent=[]
for i in range(n+1):
    parent.append(i)

def find(v):
    if parent[v]==v:
        return v
    else:
        return find(parent[v])

def merge(a,b):
    x=find(a)
    y=find(b)
    if x==y:
        return
    else:
        if x < y:
            parent[y] = x
        else:
            parent[x] = y
def judge(a,b):
    if find(a)==find(b):
        print('YES')
    else:
        print('NO')

for i in range(m):
    a,b,c=list(map(int,input().split()))
    if a==0:
        merge(b,c)
    elif a==1:
        judge(b,c)

