import sys
input=sys.stdin.readline
n,m=map(int,input().split())
data=list(map(int,input().split()))
num=[i+1 for i in range(n)]
ans=0
cur=0
for i in data:
    if len(num)==1:
        break
    temp=num.index(i)
    a=temp-cur
    b=len(num)-abs(a)
    num.pop(temp)
    if abs(a)<b:
        ans+=abs(a)
        cur=temp%len(num)
    else:
        ans+=abs(b)
        cur=temp%len(num)
print(ans)
