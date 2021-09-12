'''
import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
arr=[0]
for i in range(n):
    arr.append(int(input()))
tree=[0]*(4*n)
def init(start,end,node):
    if start==end:
        tree[node]=arr[start]
        return tree[node]
    mid=(start+end)//2
    tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
    return tree[node]
def sum(start,end,left,right,node):
    print(start,end,left,right,node)
    if right<start or left>end:
        return 0
    if left<=start and end<=right:
        return tree[node]
    mid=(start+end)//2
    return sum(start,mid,left,right,node*2)+sum(mid+1,end,left,right,node*2+1)
def update(start,end,node,index,diff):
    if index<start or end<index:
        return
    tree[node]+=diff
    if not start==end:
        mid=(start+end)//2
        update(start,mid,node*2,index,diff)
        update(mid+1,end,node*2+1,index,diff)

init(1,n,1)
for i in range(m+k):
    a,b,c=map(int,input().split())
    if a==1:
        diff=c-arr[b]
        arr[b]=c
        update(1,n,1,b,diff)
    else:
        print(sum(1,n,b,c,1))
'''

import sys
from math import ceil,log2
input=sys.stdin.readline

def init():
    for i in range(size-1,0,-1):
        tree[i]=tree[i*2]+tree[i*2+1]
def sum(start,end,left,right,node):
    print(node)
    if right<start or end<left:
        return 0
    if start<=left and right<=end:
        return tree[node]
    mid=(start+end)//2
    return sum(start,mid,left,right,node*2)+sum(mid+1,end,left,right,node*2+1)

def update(index,diff):
    temp=index+size-1
    while temp>=1:
        tree[temp]+=diff
        temp//=2


n,m,k=map(int,input().split())
size=2**ceil(log2(n))
tree=[0]*(size*2)
for i in range(n):
    tree[size+i]=int(input())
init()
for i in range(m+k):
    a,b,c=map(int,input().split())
    if a==1:
        diff=c-tree[size+b-1]
        update(b,diff)
    else:
        print(sum(1,size,b,c,1))
print(tree)