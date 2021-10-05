import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def solution(t, a, b):
    global answer

    def go(sum, visit):
        global answer
        visited[sum][visit] = True
        answer = max(answer, sum)
        if sum + a <= t and not visited[sum + a][visit]:
            go(sum + a, visit)
        if sum + b <= t and not visited[sum + b][visit]:
            go(sum + b, visit)
        if not visit and not visited[round(sum / 2)][1]:
            go(round(sum / 2), 1)

    answer = 0
    visited = [[False] * 2 for _ in range(t + 1)]
    go(0, 0)
    print(answer)
    return


if __name__ == '__main__':
    t, a, b = map(int, input().split())
    solution(t, a, b)
