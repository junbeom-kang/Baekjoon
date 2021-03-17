import sys
input=sys.stdin.readline
R=1000000007
k,n,p=map(int,input().split())
for i in range(p):
    k=(k*n)%R
print(k)