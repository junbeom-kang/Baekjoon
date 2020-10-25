import sys
input=sys.stdin.readline
n,m=map(int,input().split())
def divide(a,b):
    if b==1:
        return a%p
    elif b%2==1:
        return divide((a**2)%p,b//2)*a%p
    else:
        return divide((a**2)%p,b//2)
p=1000000007
a=1
b=1
t=min(n-m,m)
for i in range(t):
    a=a*(n-i)%p
    b=b*(t-i)%p
print((a*divide(b,p-2))%p)
#페르마의 소정리
# (A/B) % p
# = A * B^-1 % p
# = A * B^-1 * B^p-1 % p
# = A * B^p-2 % p
# = (A % p) * (B^p-2 % p) % p