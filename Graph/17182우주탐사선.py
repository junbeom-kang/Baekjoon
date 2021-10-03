import sys

input = sys.stdin.readline
INF = sys.maxsize


def solution(arr):
    global answer

    def go(v, m):
        global answer
        if m==((1<<n)-1):
            return 0

        elif dp[v][m]!=INF:
            return dp[v][m]
        else:
            temp=INF
            for i in range(n):
                if not m & (1 << i):
                    temp=min(temp,go(i,m+(1<<i))+arr[v][i])
            dp[v][m]=temp
            return dp[v][m]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if arr[i][j] > arr[i][k] + arr[k][j]:
                    arr[i][j] = arr[i][k] + arr[k][j]
    dp=[[INF]*(2**n) for _ in range(n)]
    answer = INF
    go(m, 1<<m)
    print(dp[m][1<<m])
    return


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    solution(arr)
