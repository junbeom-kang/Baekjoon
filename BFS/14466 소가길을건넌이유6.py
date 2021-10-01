import sys
from collections import deque

input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solution():
    answer = set()
    for i in range(len(cow) - 1):
        visited = [[False] * (n+1) for _ in range(n+1)]
        q = deque([])
        q.append(cow[i])
        visited[cow[i][0]][cow[i][1]] = True
        while q:
            x, y = q.popleft()
            for t in range(4):
                nx = x + dx[t]
                ny = y + dy[t]
                if (1 <= nx <= n and 1 <= ny <=n) and (x, y, nx, ny) not in block and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])

        for j in range(i + 1, len(cow)):
            if not visited[cow[j][0]][cow[j][1]]:
                if cow[i][0] < cow[j][0]:
                    answer.add((cow[i][0], cow[i][1], cow[j][0], cow[j][1]))
                elif cow[i][0] > cow[j][0]:
                    answer.add((cow[j][0], cow[j][1], cow[i][0], cow[i][1]))
                else:
                    if cow[i][1] < cow[j][1]:
                        answer.add((cow[i][0], cow[i][1], cow[j][0], cow[j][1]))
                    else:
                        answer.add((cow[j][0], cow[j][1], cow[i][0], cow[i][1]))

    print(len(answer))

    return


if __name__ == '__main__':
    n, k, r = map(int, input().split())
    block = set()
    cow = []
    for i in range(r):
        x, y, x1, y1 = map(int, input().split())
        block.add((x, y, x1, y1))
        block.add((x1, y1, x, y))
    for i in range(k):
        cow.append(list(map(int, input().split())))
    solution()
