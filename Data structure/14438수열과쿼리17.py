import sys
from math import ceil,log2
input=sys.stdin.readline
INF=sys.maxsize
def init():
    for i in range(size-1,0,-1):
        tree[i]=min(tree[i*2],tree[i*2+1])
def find(start,end,left,right,node):
    if right<start or end<left:
        return INF
    if left<=start and end<=right:
        return tree[node]
    mid=(start+end)//2
    return min(find(start,mid,left,right,node*2),find(mid+1,end,left,right,node*2+1))

def update(index):
    while index>=1:
        tree[index]=min(tree[index*2],tree[index*2+1])
        index//=2


n=int(input())
size=2**ceil(log2(n))
tree=[0]*(size*2)
temp=list(map(int,input().split()))
m=int(input())
for i in range(n):
    tree[size+i]=temp[i]
init()
for i in range(m):
    a,b,c=map(int,input().split())
    if a==1:
        tree[size+b-1]=c
        update((size+b-1)//2)
    else:
        print(find(1,size,b,c,1))
