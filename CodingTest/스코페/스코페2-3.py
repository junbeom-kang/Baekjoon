#최소공통조상
import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
def find(v):
    if uptree[v]==0:
        return v
    else:
        return find(uptree[v])

def DFS(v, d):
    check[v] = True
    depth[v] = d
    for i in tree[v]:
        if check[i]:
            continue
        else:
            dp[0][i] = v
            DFS(i, d + 1)


n,q =map(int,input().split())
logn = int(math.ceil(math.log2(n)))
dp = [[0] * (500001) for _ in range(logn + 1)]
tree = [[] for _ in range(500001)]
uptree = [0]*(500001)

for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    uptree[b]=a
depth = [0] * (500000 + 1)
check = [False] * (500000 + 1)
DFS(find(b), 0)

for i in range(1, logn + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i - 1][dp[i - 1][j]]
for i in range(q):
    a, b = map(int, input().split())
    if depth[a]>depth[b]:
        print("no")
        continue
    for i in range(logn, -1, -1):
        if depth[b] - depth[a] >= 1 << i:
            b = dp[i][b]
    if a == b:
        print("yes")
        continue
    else:
        print("no")
    #for i in range(logn, -1, -1):
    #    if dp[i][a] != dp[i][b]:
    #        a = dp[i][a]
    #        b = dp[i][b]