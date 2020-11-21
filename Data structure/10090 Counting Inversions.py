import sys
from math import ceil,log2
input=sys.stdin.readline
def find(start,end,left,right,node):
    if start>right or end<left:
        return 0
    if left<=start and end<=right:
        return tree[node]
    mid=(start+end)//2
    return find(start,mid,left,right,node*2)+find(mid+1,end,left,right,node*2+1)

def update(node):
    temp=size+node-1
    while temp>=1:
        tree[temp]+=1
        temp//=2
n=int(input())
data=list(map(int,input().split()))
size=2**ceil(log2(n))
tree=[0]*(size*2)
ans=0
for i in data:
    ans+=find(1,size,i+1,size,1)
    update(i)

print(ans)