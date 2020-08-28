import sys
input=sys.stdin.readline
n=int(input())
dp=[0]*(n+1)
for i in range(2,n+1):
    temp=dp[i-1]
    if i%3==0 and dp[i//3]<temp:
        dp[i]=dp[i//3]+1
    elif i%2==0 and dp[i // 2] < temp:
        dp[i] = dp[i // 2] + 1
    else:
        dp[i]=temp+1
print(dp[n])
while n!=1:
    print(n,end=' ')
    temp=dp[n-1]
    if n%3==0 and dp[n//3]<temp:
        n//=3
    elif n%2==0 and dp[n//2]<temp:
        n//=2
    else:
        n-=1
print(1)