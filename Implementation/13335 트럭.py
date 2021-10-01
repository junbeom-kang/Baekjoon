import sys
from collections import deque

input = sys.stdin.readline


def solution():
    c = deque(car)
    q = deque()
    q.append([c.popleft(), 0])
    cnt = 1
    sum = car[0]
    while c:
        for i in q:
            i[1] += 1

        if q[0][1] == w:
            sum -= q[0][0]
            q.popleft()
        if sum + c[0] <= l:

            sum += c[0]
            q.append([c.popleft(),0])

        cnt += 1

    cnt += w
    print(cnt)
    return


if __name__ == '__main__':
    n, w, l = map(int, input().split())
    car = list(map(int, input().split()))
    solution()
