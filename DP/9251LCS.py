import sys
input=sys.stdin.readline
stack=input().strip()
s=len(stack)
verses=input().strip()
v=len(verses)
dp=[[0 for _ in range(v+1)]for _ in range(s+1)]
for i in range(1,s+1):
    for j in range(1,v+1):
        if stack[i-1]==verses[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[s][v])
