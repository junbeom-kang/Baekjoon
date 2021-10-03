# 설정한 수보다 크면 1
from heapq import heappush, heappop
import sys

input = sys.stdin.readline
INF = sys.maxsize


def solution():
    global can

    def dijkstra(v, k):
        global can
        q = []
        ans = [INF] * (n + 1)
        ans[n]=0
        heappush(q, (0, n))
        while q:
            w, c = heappop(q)
            if w > k:
                break
            if c == 1:
                can = True
                break
            for where, weight in arr[c]:
                if w!=ans[c]:
                    continue
                if weight > v:
                    if ans[where]>ans[c]+1:
                        ans[where]=ans[c]+1
                        heappush(q,(ans[c]+ 1, where))
                else:
                    if ans[where]>ans[c]:
                        ans[where]=ans[c]
                        heappush(q, (ans[c], where))

    answer = -1
    left = 0
    right = 1000000
    while left <= right:
        can = False
        mid = (left + right) // 2
        dijkstra(mid, k)
        if can:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    print(answer)
    return


if __name__ == '__main__':
    n, p, k = map(int, input().split())
    arr = [[] for _ in range(n + 1)]
    for i in range(p):
        a, b, w = map(int, input().split())
        arr[a].append((b, w))
        arr[b].append((a, w))
    solution()
