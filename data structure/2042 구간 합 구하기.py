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