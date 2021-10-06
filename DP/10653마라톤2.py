import sys

input = sys.stdin.readline
INF = sys.maxsize


def solution(arr):
    dp = [[INF] * ( k+ 1) for _ in range(n+1)]
    dp[0][0] =0
    for i in range(n):
        for j in range(k+1):
            for q in range(j+1):
                if i-q-1>=0:
                    dp[i][j]=min(dp[i][j],dp[i-q-1][j-q]+abs(arr[i-q-1][0]-arr[i][0])+abs(arr[i-q-1][1]-arr[i][1]))
    print(min(dp[n-1]))
    return


if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(tuple(map(int, input().split())))

    solution(arr)
