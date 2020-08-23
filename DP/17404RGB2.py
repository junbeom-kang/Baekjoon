import sys
input=sys.stdin.readline
n=int(input())
stack=[list(map(int,input().split())) for _ in range(n)]
INF=sys.maxsize
def go(start):
    dp=[INF]*3
    newdp=[0]*3
    dp[start]=stack[0][start]
    newdp[start]=INF
    for i in range(1,n):
        for j in range(3):
            if i==1 and j==start:
                continue
            if i==n-1 and j==start:
                continue
            if j==0:
                newdp[j]=min(dp[1]+stack[i][j],dp[2]+stack[i][j])
            elif j==1:
                newdp[j]=min(dp[0]+stack[i][j],dp[2]+stack[i][j])
            else:
                newdp[j]=min(dp[0]+stack[i][j],dp[1]+stack[i][j])
        if i==n-1:
            newdp.pop(start)
            return min(newdp)
        dp=newdp
        newdp=[0]*3
ans=INF
for i in range(3):
    ans=min(go(i),ans)
print(ans)