#기저사례 체크
import sys
input=sys.stdin.readline
n=int(input())
arr=input().rstrip()
dp=[0]*n
dp[0]=1
if arr[1]=='1':
    dp[1]=1
for i in range(2,n):
    if arr[i]=='0':
        continue
    if arr[i-1] and arr[i-2]:
        dp[i]=dp[i-1]+dp[i-2]
    else:
        if arr[i-1]:
            dp[i]=dp[i-1]
        else:
            dp[i]=dp[i-2]
print(dp[n-1])

