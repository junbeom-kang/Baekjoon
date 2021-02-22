import sys
input=sys.stdin.readline
n,m=map(int,input().split())
arr=list(map(int,input().split()))
ans=0
right=0
temp=0
for i in arr:
    while temp<m and right<n:
        temp+=arr[right]
        right+=1
    if temp==m:
        ans+=1
    temp-=i

print(ans)

