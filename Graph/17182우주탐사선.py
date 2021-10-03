import sys

input = sys.stdin.readline
INF = sys.maxsize


def solution(arr):
    global answer

    def go(v, m, cnt, sum):
        global answer
        if cnt == n:
            answer = min(answer, sum)
        else:
            for i in range(n):
                if not v & (1 << i):
                    go(v + (1 << i), i, cnt + 1, sum + arr[m][i])

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if arr[i][j] > arr[i][k] + arr[k][j]:
                    arr[i][j] = arr[i][k] + arr[k][j]
    answer = INF
    go(1 << m, m, 1, 0)
    print(answer)
    return


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    solution(arr)
