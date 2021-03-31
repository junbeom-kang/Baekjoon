import sys
R=1000000007
input=sys.stdin.readline
p,n=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(1,n):
    arr[i]=(arr[i-1]*3+arr[i])%R
print(arr[n-1])