import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
#0은 없을 때,1은 멘티일 때,2는 멘토일 때
def dfs(v):
    for i in tree[v]:
        dfs(i)
        dp[v][0]+=dp[i][2]
        dp[v][1]+=max(dp[i][0],dp[i][2])
    temp=dp[v][1]
    for i in tree[v]:
        dp[v][2]=max(dp[v][2],temp-max(dp[i][0],dp[i][2])+dp[i][1]+w[v]*w[i])


n=int(input())
tree=[[] for _ in range(n+1)]
for i,d, in enumerate(list(map(int,input().split())),2):
    tree[d].append(i)
dp=[[0]*3 for _ in range(n+1)]
w=[0]+list(map(int,input().split()))
dfs(1)
print(max(dp[1]))