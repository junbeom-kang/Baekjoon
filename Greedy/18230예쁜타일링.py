import sys
def input():
    return sys.stdin.readline()
n,a,b=list(map(int,input().split()))
one=sorted(list(map(int,input().split())),reverse=True)
two=sorted(list(map(int,input().split())),reverse=True)
temp=0
for i in range(b+1):
    ans = 0
    N1=n-2*i
    if N1>a or N1<0:
        continue
    ans=sum(one[:N1])+sum(two[:i])
    temp=max(temp,ans)
print(temp)