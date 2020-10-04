import sys
import math
input=sys.stdin.readline
n=int(input())
stack=[]

for _ in range(n):
    stack.append(int(input()))
stack.sort()
gcd=stack[-1]-stack[0]
for i in range(n):
    gcd=math.gcd(stack[i]-stack[i-1],gcd)
s=set()
s.add(gcd)
for i in range(2,int(gcd**0.5)+1):
    if gcd%i==0:
        s.add(i)
        s.add(gcd//i)
s=list(s)
print(*sorted(s))