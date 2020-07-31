import sys
input=sys.stdin.readline
n=int(input())
data=list(map(int,input().split()))
dp=[0]*len(data)
dp[0]=data[0]
for i in range(1,n):
    if dp[i-1]<0:
        dp[i]=data[i]
    else:
        dp[i]=dp[i-1]+data[i]
print(max(dp))