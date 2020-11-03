import sys
input=sys.stdin.readline
n,m=map(int,input().split())
arr=[0]+list(map(int,input().split()))
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

init(1,n,1)
for i in range(m):
    a,b=map(int,input().split())
    print(sum(1,size,a,b,1))