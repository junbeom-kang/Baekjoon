import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def solution(arr):
    def find(v):
        if parent[v] == v:
            return v
        else:
            parent[v] = find(parent[v])
            return parent[v]

    def merge(q, w):
        if q <= w:
            parent[w] = q
        else:
            parent[q] = w

    parent = [i for i in range(n + 1)]
    q = []
    for i in range(n):
        for j in range(i + 1, n):
            heappush(q, (arr[i][j], (i, j)))
    cnt = 0
    sum = 0
    while cnt < n - 1:
        weight, (x, y) = heappop(q)
        w1 = find(x)
        w2 = find(y)
        if w1 != w2:
            merge(w1, w2)
            cnt += 1
            sum += weight
    print(sum)

    return


if __name__ == '__main__':
    n = int(input())

    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    solution(arr)
