import sys
input=sys.stdin.readline
def powernumber(a,b):
    cnt=1
    while a>b:
        if a%b==0:
            a//=b
            cnt+=1
        else:
            return 0
    if a==b:
        return cnt
    else:
        return 0

def pisano(m):
    a=powernumber(m,2)
    if a and a>2 and a%2==0:
        return (2**(a-1))*3
    b=powernumber(m,5)
    if b and b>2 and b%2==0:
        return 4*(5**b)
    if m%2==0:
        c=powernumber(m//2,5)
        if c and c>2 and c%2==0:
            return 6*m
    d=powernumber(m,10)
    if d and d>2 and d%2==0:
        return 15*(10**(d-1))
    x,y=1,1
    for i in range(3,m**2+2):
        x,y=y,(x+y)%m
        if x==1 and y==1:
            return i-2

t=int(input())
for i in range(1,t+1):
    _,n=map(int,input().split())
    print(i,pisano(n))
