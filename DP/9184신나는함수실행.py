import sys
def w(a,b,c):
    if dp[a][b][c]:
        return dp[a][b][c]
    if a <= 50 or b <= 50 or c <= 50:
        dp[a][b][c]=1
        return dp[a][b][c]
    if a > 70 or b > 70 or c > 70:
        dp[a][b][c]=w(70,70,70)
        return dp[a][b][c]
    if  a < b and b < c:
        dp[a][b][c]=w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c]=w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]

input=sys.stdin.readline
dp=[[[0]*101 for _ in range(101)] for _ in range(101)]
while(True):
    a,b,c=map(int,input().split())
    if a==-1 and b==-1 and c==-1:
        break
    print("w(%d, %d, %d) = %d"%(a,b,c,w(a+50,b+50,c+50)))
