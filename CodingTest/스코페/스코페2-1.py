import sys
input=sys.stdin.readline

n,temp=input().split()
n=int(n)
dp=[0]*(n+1)
arr=[0]*(n+1)
h,m,s=map(int,temp.split(":"))
total=h*3600+m*60+s
for i in range(1,n+1):
    m,s=map(int,input().split(":"))
    arr[i]=m*60+s
sum=0
cnt=0
j=1
for i in range(1,n+1):
    while sum<total:
        if j==n+1:
            break
        sum+=arr[j]
        cnt+=1
        j+=1
    dp[i]=cnt
    sum-=arr[i]
    cnt-=1
ans=max(dp[1::])
for i in range(1,len(dp)):
    if dp[i]==ans:
        print(dp[i],i)
        break
