import sys

input = sys.stdin.readline


def solution(first, second):
    def change(arr):
        for k in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    if not arr[i][j]:
                        if arr[i][k] and arr[k][j]:
                            arr[i][j] = True

    change(first)
    change(second)
    for i in range(1, n + 1):
        sum = 0
        for j in range(1, n + 1):
            if first[i][j] or second[i][j]:
                sum += 1
        print(n - sum)

    return


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    first = [[False] * (n + 1) for _ in range(n + 1)]
    second = [[False] * (n + 1) for _ in range(n + 1)]
    for i in range(m):
        temp1, temp2 = map(int, input().split())
        first[temp1][temp2] = True
        second[temp2][temp1] = True
    for i in range(1, n + 1):
        first[i][i] = True
        second[i][i] = True
    solution(first, second)
