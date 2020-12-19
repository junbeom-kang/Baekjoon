import sys,math
INF=sys.maxsize
input=sys.stdin.readline
n=int(input())
arr=[INF]*(n+1)
t=int(math.sqrt(n))
for i in range(1,t+1):
    arr[i**2]=1
for i in range(2,n+1):
    temp=int(math.sqrt(i))
    for j in range(1,temp+1):
        arr[i]=min(arr[i],1+arr[i-(j**2)])
print(arr[n])