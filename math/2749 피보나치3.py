import sys
input=sys.stdin.readline
n=int(input())
p=1000000
x=[1,1]
while 1:
    x.append((x[-1]+x[-2])%p)
    if x[-2]==1 and x[-1]==1:
        break
t=len(x)-2
n=n%t
print(x[n-1])