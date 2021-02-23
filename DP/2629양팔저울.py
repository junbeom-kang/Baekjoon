import sys
sys.setrecursionlimit(10**6)
def DFS(count,Weight):
    if count==n:
        return
    if dp[count][Weight+15000]:
        return
    dp[count][Weight+15000]=True
    check[abs(Weight)]=True

    DFS(count+1,Weight+weight[count])
    DFS(count+1,Weight)
    DFS(count+1,Weight-weight[count])

input=sys.stdin.readline
n=int(input())
weight=list(map(int,input().split()))
m=int(input())
ball=list(map(int,input().split()))
dp=[[False]*30001 for _ in range(n)]
check=[False]*15001

ans=[]
DFS(-1,0)
for i in ball:
    if i>15000:
        ans.append("N")
    else:
        if check[i]:
            ans.append("Y")
        else:
            ans.append("N")
print(*ans)

