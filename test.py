import sys
from collections import defaultdict

input = sys.stdin.readline


def solution(t, n, m, first, second):
    fd, sd = defaultdict(int), defaultdict(int)
    fd[0], sd[0] = 1, 1
    fd[sum(first)],sd[sum(second)]=1,1
    for i in range(n):
        temp = 0
        for j in range(i, i+n-1):
            temp += first[j%n]
            fd[temp] += 1
    for i in range(m):
        temp = 0
        for j in range(i, i+m-1):
            temp += second[j%m]
            sd[temp] += 1
    answer = 0
    for i in fd.keys():
        if i > t:
            continue
        else:
            if t - i in sd:
                answer += sd[t - i] * fd[i]
    print(answer)

    return


if __name__ == '__main__':
    t = int(input())
    n, m = map(int, input().split())
    first = []
    second = []
    for i in range(n):
        first.append(int(input()))
    for i in range(m):
        second.append(int(input()))
    solution(t, n, m, first, second)
