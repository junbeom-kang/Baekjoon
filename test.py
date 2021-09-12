from heapq import heappush, heappop


def solution():
    def find(v):
        if parent[v] == v:
            return v
        else:
            parent[v] = find(parent[v])
            return parent[v]

    def union(q, w):
        print(q,w)
        if q < w:
            parent[w] = q
        else:
            parent[q] = w

    answer = 0

    n, m = map(int, input().split())
    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i
    heap = []
    for i in range(m):
        a, b, c = map(int, input().split())
        heappush(heap, (c, a, b))
    print("hi")
    i = 0
    while i != n - 1:
        print(c)
        c, a, b = heappop(heap)
        q = find(a)
        w = find(b)
        print(q,w)
        if q != w:
            answer += c
            union(q, w)
            i += 1

    print(parent)
    print(answer)
    return answer


solution()