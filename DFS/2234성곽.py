import sys

input = sys.stdin.readline
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def solution(arr):
    global big

    def DFS(x, y):
        global big
        visited[x][y] = True
        number[x][y] = cnt
        big += 1
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and not wall[x][y][t]:
                DFS(nx, ny)

    answer = 0
    bigbig = 0
    visited = [[False] * m for _ in range(n)]
    number = [[0] * m for _ in range(n)]
    wall = [[[False] * 4 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(4):
                if arr[i][j] & (1 << k):
                    wall[i][j][k] = True

    cnt = 1
    dic = {}
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                big = 0
                DFS(i, j)
                dic[cnt] = big
                cnt += 1
                bigbig = max(big, bigbig)

    for i in range(n):
        for j in range(m - 1):
            if number[i][j] != number[i][j + 1]:
                answer = max(answer, dic[number[i][j]] + dic[number[i][j + 1]])
    for i in range(n-1):
        for j in range(m):
            if number[i][j] != number[i+1][j]:
                answer = max(answer, dic[number[i][j]] + dic[number[i + 1][j]])
    print(cnt-1)
    print(bigbig)
    print(answer)

    return


if __name__ == '__main__':
    m, n = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    solution(arr)
