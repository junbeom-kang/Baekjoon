import sys

input = sys.stdin.readline


def solution():
    def find(v):
        if parent[v] == v:
            return v
        else:
            parent[v] = find(parent[v])
            return parent[v]

    def merge(a, b):
        q = find(a)
        w = find(b)
        if q == w:
            return
        else:
            if q <= w:
                parent[w] = q
            else:
                parent[q] = w

    bad = [set() for _ in range(n + 1)]
    for i in range(m):
        a, b, c = input().split()
        if a == 'E':
            bad[int(b)].add(int(c))
            bad[int(c)].add(int(b))
        else:
            merge(int(b), int(c))
    for i in range(1, n + 1):
        if len(bad[i]) > 1:
            for x, y in enumerate(bad[i]):
                if x == 1:
                    break
                temp = y
            for x in bad[i]:
                merge(temp, x)
    for i in range(1, n + 1):
        find(i)
    print(len(set(parent))-1)

    return


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    parent = [i for i in range(n + 1)]

    solution()
