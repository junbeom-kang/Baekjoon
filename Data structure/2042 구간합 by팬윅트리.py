import sys
input=sys.stdin.readline

def update(v,d):
    while v<n+1:
        tree[v]+=d
        v+=(v&-v)
def tsum(v):
    num=0
    while v>0:
        num+=tree[v]
        v-=(v&-v)
    return num

n,m,k=map(int,input().split())
arr=[0]
for i in range(n):
    arr.append(int(input()))
tree=[0]*(n+1)
for i in range(1,n+1):
    update(i,arr[i])
for i in range(m+k):
    a,b,c=map(int,input().split())
    if a==1:
        diff=c-arr[b]
        arr[b]=c
        update(b,diff)
    else:
        print(tsum(c)-tsum(b-1))
