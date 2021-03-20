import sys

INF = sys.maxsize
input = sys.stdin.readline


def DFS(x, y, cnt):
    if 0 <= y - 1:
        if arr[x][y - 1] == '.' and dp[x][y - 1] > cnt + 1:
            dp[x][y - 1] = cnt + 1
            DFS(x, y - 1, cnt + 1)
    if y + 1 <= m - 1:
        if arr[x][y + 1] == '.' and dp[x][y + 1] > cnt + 1:
            dp[x][y + 1] = cnt + 1
            DFS(x, y + 1, cnt + 1)
    if x + 1 <= n - 1:
        if arr[x + 1][y] == '.' and dp[x + 1][y] > cnt:
            dp[x + 1][y] = cnt
            DFS(x + 1, y, cnt)


m, n = map(int, input().split())
arr = [[] for _ in range(n)]
dp = [[INF] * m for _ in range(n)]
for i in range(n):
    arr[i] = list(input().rstrip())
start = []
for i in range(m):
    if arr[0][i] == 'c':
        dp[0][i] = 0
        start.append((0, i))
for i in start:
    DFS(i[0], i[1], 0)
temp = min(dp[n - 1])
if temp == INF:
    print('-1')
else:
    print(temp)
