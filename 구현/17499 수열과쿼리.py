import sys
input=sys.stdin.readline
N,Q=map(int,input().split())
list1=list(map(int,input().split()))
start=0
for _ in range(Q):
    a=list(map(int,input().split()))
    if a[0]==1:
        _,p,x=a
        list1[(start+a[1]-1)%N]+=a[2]
    elif a[0]==2:
        start=(start-a[1])%N
    else:
        start=(start+a[1])%N
print(*list1[start::],*list1[0:start])
