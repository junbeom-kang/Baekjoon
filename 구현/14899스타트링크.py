import sys
import itertools
input=sys.stdin.readline
n=int(input())
number=set([i for i in range(n)])
adj=[list(map(int,input().split()))for _ in range(n)]
min_value=float('inf')
x=list(itertools.combinations(number,n//2))
for i in range(len(x)//2):
    lsum=0
    rsum=0
    for j in x[i]:
        for m in x[i]:
            if adj[j][m]==0:
                continue
            else:
                lsum+=adj[j][m]
    temp=number-set(x[i])
    for j in temp:
        for m in temp:
            if adj[j][m] == 0:
                continue
            else:
                rsum += adj[j][m]
    min_value=min(min_value,abs(lsum-rsum))
print(min_value)
print(range(4))
