import sys
N, K, R = map(int, input().split())
graph = [[0 for c in range(N+1)] for r in range(N+1)]
walls = [[[] for c in range(N+1)] for r in range(N+1)]
dire = (-1, 0, 1, 0)

for _ in range(R):
    r1,c1,r2,c2 = map(int, sys.stdin.readline().split())
    walls[r1][c1].append((r2-r1, c2-c1))
    walls[r2][c2].append((r1-r2, c1-c2))
for _ in range(K):
    r,c = map(int, input().split())
    graph[r][c] = 1

def dfs(r, c):
    ret = graph[r][c]
    graph[r][c] = -1
    tmp = 0
    for i in range(4):
        if (dire[i], dire[3-i]) in walls[r][c]: continue
        nr, nc = r+dire[i], c+dire[3-i]
        if 1 <= nr <= N and 1 <= nc <= N and graph[nr][nc] != -1:
            tmp += dfs(nr, nc)
    return ret + tmp

group = []
for r in range(1, N+1):
    for c in range(1, N+1):
        if graph[r][c] != -1:
            group.append(dfs(r, c))
cumsum = 0
answer = 0
print(group)
for cur in group:
    cumsum += cur
    answer += cur * (K-cumsum)
print(answer)