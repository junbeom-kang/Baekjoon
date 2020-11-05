import sys
from math import ceil,log2
input=sys.stdin.readline
INF=sys.maxsize
def init():
    for i in range(size-1,0,-1):
        tree[i]=(min(tree[2*i][0],tree[2*i+1][0]),max((tree[2*i][1],tree[2*i+1][1])))
def find(start,end,left,right,node):
    if left>end or right<start:
        return (INF,-INF)
    if left<=start and end<=right:
        return tree[node]
    mid=(start+end)//2
    q=find(start, mid, left, right, node * 2)
    w=find(mid + 1, end, left, right, node * 2 + 1)
    return (min(q[0],w[0]),max(q[1],w[1]))
def update(i):
    while i>=1:
        tree[i]=(min(tree[2*i][0],tree[2*i+1][0]),max((tree[2*i][1],tree[2*i+1][1])))
        i//=2

T=int(input())
for _ in range(T):
    n,m=map(int,input().split())
    size=2**ceil(log2(n))
    tree=[(INF,-INF)for _ in range(2*size)]
    for i in range(n):
        tree[size+i]=(i,i)
    init()
    for i in range(m):
        a,b,c=map(int,input().split())
        if a==1:
            temp=find(0,size-1,b,c,1)
            if temp[0]==b and temp[1]==c:
                print('YES')
            else:
                print('NO')
        else:
            q=tree[size+b]
            w=tree[size+c]
            tree[size+b]=w
            tree[size+c]=q
            update((size+b)//2)
            update((size+c)//2)