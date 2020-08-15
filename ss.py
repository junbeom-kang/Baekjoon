# https://www.acmicpc.net/problem/2206
import sys

I = sys.stdin.readline


def bfs():
    que = [(0, 0, False)]
    count = 1
    while que:
        que_ = []
        for r, c, flag in que:
            if r == R - 1 and c == C - 1:
                return count
            for dr, dc in dir:
                rr = r + dr
                cc = c + dc
                if 0 <= rr < R and 0 <= cc < C:
                    if not flag:
                        if not visitF[rr][cc]:
                            if Map[rr][cc] == '0':
                                visitF[rr][cc] = True
                                que_.append((rr, cc, False))
                            else:
                                visitF[rr][cc] = True
                                que_.append((rr, cc, True))
                    else:
                        if not visitT[rr][cc]:
                            if Map[rr][cc] == '0':
                                visitT[rr][cc] = True
                                que_.append((rr, cc, True))

        que = que_
        count += 1
    return -1


dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
R, C = list(map(int, I().split()))
Map = [list(I()) for _ in range(R)]
visitF = [[False] * C for _ in range(R)]
visitT = [[False] * C for _ in range(R)]

print(bfs())
