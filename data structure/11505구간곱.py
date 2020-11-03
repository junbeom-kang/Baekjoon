import sys
from math import ceil,log2
input=sys.stdin.readline
p= 1000000007
def init():
    for i in range(size-1,0,-1):
        tree[i]=(tree[i*2]*tree[i*2+1])%p
def mult(start,end,left,right,node):
    if right<start or end<left:
        return 1
    if left<=start and end<=right:
        return tree[node]
    mid=(start+end)//2
    return (mult(start,mid,left,right,node*2)*mult(mid+1,end,left,right,node*2+1))%p

def update(node):
    while node>=1:
        tree[node]=(tree[node*2]*tree[node*2+1])%p
        node//=2


n,m,k=map(int,input().split())
size=2**ceil(log2(n))
tree=[1]*(size*2)
for i in range(n):
    tree[size+i]=int(input())
init()
for i in range(m+k):
    a,b,c=map(int,input().split())
    if a==1:
        tree[size+b-1]=c
        update((size+b-1)//2)
    else:
        print(mult(1,size,b,c,1))