import sys
input=sys.stdin.readline
n=int(input())
stack=[]
dp=[0]*n
dp[0]=1
for i in range(n):
    stack.append(list(map(int,input().split())))
stack.sort()
for i in range(1,n):
    for j in range(i):
        if stack[j][1]<stack[i][1] and dp[j]>dp[i]:
            dp[i]=dp[j]
    dp[i]+=1
print(dp)
print(n-max(dp))