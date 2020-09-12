import sys
input=sys.stdin.readline
INF=sys.maxsize
def solution(n, s, a, b, fares):
    arr=[[INF]*(n+1) for _ in range(n+1)]
    for i in fares:
        arr[i[0]][i[1]]=i[2]
        arr[i[1]][i[0]]=i[2]
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    arr[i][j] = 0
                    continue
                arr[i][j] = min(arr[i][k] + arr[k][j], arr[i][j])
    dp=[INF]*n
    for i in range(n):
        dp[i]=arr[s][i+1]+arr[i+1][a]+arr[i+1][b]
    answer = min(dp)
    return answer