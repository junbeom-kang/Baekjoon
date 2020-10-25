import sys
input=sys.stdin.readline
n,m=map(int,input().split())
def divide(a,b):
    if b==1:
        return a
    elif b%2==0:
        return (divide(a,b//2)**2)%p
    else:
        return (divide(a,b//2)**2*a)%p

p=1000000007
dp=[1]*(n+1)
for i in range(2,n+1):
    dp[i]=dp[i-1]*i%p
print((dp[n]*divide(dp[n-m]*dp[m],p-2))%p)









# (A/B) % p
# = A * B^-1 % p
# = A * B^-1 * B^p-1 % p
# = A * B^p-2 % p
# = (A % p) * (B^p-2 % p) % p