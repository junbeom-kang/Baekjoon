import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def solution(arr, n, m):
    global cnt, can

    def dfs(x, y, z):
        global cnt, can
        visited[z][x][y] = True
        cnt += 1
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                can = False
                continue
            if arr[nx][ny] < z and not visited[z][nx][ny]:
                dfs(nx, ny, z)

    visited = [[[False] * m for _ in range(n)] for _ in range(10)]
    answer = 0
    for k in range(1, 10):
        for i in range(n):
            for j in range(m):
                if not visited[k][i][j] and arr[i][j]<k:
                    cnt = 0
                    can = True
                    dfs(i, j, k)
                    if can:
                        answer += cnt
    print(answer)

    return


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().rstrip())))
    solution(arr, n, m)
