import sys
input=sys.stdin.readline
first=list(input().rstrip())
second=list(input().rstrip())
lf=len(first)
ls=len(second)
dp=[[0]*(lf+1)for _ in range(ls+1)]
for i in range(1,ls+1):
    for j in range(1,lf+1):
        if first[j-1]==second[i-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[ls][lf])
temp=dp[ls][lf]
ans=[]
x=ls+1
y=lf+1
for i in range(ls,-1,-1):
    for j in range(lf,-1,-1):
        if i>=x or j>=y:
            continue
        if dp[i][j]!=dp[i][j-1] and dp[i][j]!=dp[i-1][j] and dp[i][j]==temp:
            ans.append(second[i-1])
            x=i
            y=j
            temp-=1
print(''.join(map(str,ans[::-1])))