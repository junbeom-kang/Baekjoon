import sys
input=sys.stdin.readline
n,m=list(map(int,input().split()))
coin=[]
count=0
for i in range(n):
    coin.append(int(input()))
a=coin.pop()
while m!=0:
    if a>m:
        a=coin.pop()
    else:
        q=m//a
        m=m%a
        count=count+q
print(count)