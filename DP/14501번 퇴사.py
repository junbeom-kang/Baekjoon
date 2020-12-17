import sys
input=sys.stdin.readline
n=int(input())
data=[0]
time=[0]
for i in range(n):
    a,b=map(int,input().split())
    time.append(a)
    data.append(b)
dp=[0]*(n+1)
if time[1]==1:
    dp[1]=data[1]
for i in range(2,n+1):
    temp = []
    for j in range(1,i+1):
        if time[j]+j-1<=i:
            temp.append(data[j]+dp[j-1])
    if temp:
        dp[i]=max(max(temp),dp[i])
print(max(dp))