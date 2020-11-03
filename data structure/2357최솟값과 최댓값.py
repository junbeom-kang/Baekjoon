import sys
from math import log2,ceil
INF=sys.maxsize
input=sys.stdin.readline



def init():
    for i in range(size-1,0,-1):
        tree[i]=(min(tree[i*2][0],tree[i*2+1][0]),max(tree[i*2][1],tree[i*2+1][1]))

def find(start,end,left,right,node):
    global a,b
    if right<start or left>end:
        return
    if left<=start and end<=right:
        a,b=min(a,tree[node][0]),max(b,tree[node][1])
        return
    mid=(start+end)//2
    find(start,mid,left,right,node*2)
    find(mid+1,end,left,right,node*2+1)

n,m=map(int,input().split())

size=2**ceil(log2(n))
tree=[(INF,-INF)]*(size*2)
for i in range(n):
    temp=int(input())
    tree[size+i]=(temp,temp)
init()
for i in range(m):
    a,b=INF,-INF
    q,w=map(int,input().split())
    find(1,size,q,w,1)
    print(a,b)