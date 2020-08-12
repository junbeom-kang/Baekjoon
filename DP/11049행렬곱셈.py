import sys
input=sys.stdin.readline
n=int(input())
stack=[]
dp=[[sys.maxsize for _ in range(n)]for _ in range(n)]
for i in range(n):
    stack.append(list(map(int,input().split())))
    dp[i][i]=0
for d in range(1,n):
    for i in range(n-d):
        for mid in range(i,i+d):
            dp[i][i+d]=min(stack[i][0]*stack[mid][1]*stack[i+d][1]+dp[i][mid]+dp[mid+1][i+d],dp[i][i+d])
print(dp[0][-1])
