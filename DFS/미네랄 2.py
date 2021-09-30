import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solution(arr, spear):
    global can
    def godown(s,l):
        ret = sys.maxsize
        for x1,y1 in s:
            for q in range(x1 + 1, n + 1):
                if q == n:
                    ret = min(ret, n - x1 - 1)
                else:
                    if arr[q][y1] == 'x' and (q,y1)not in l:
                        ret = min(ret, q - x1 - 1)
                        break
        return ret

    def DFS(x, y):
        global can
        l.add((x, y))
        if x<n-1 and arr[x+1][y]=='.':
            s.add((x,y))
        visited[x][y] = True
        for p in range(4):
            nx = x + dx[p]
            ny = y + dy[p]
            if nx == n:
                can = True
            elif 0 <= nx < n and 0 <= ny < m and arr[nx][ny]=='x' and not visited[nx][ny]:
                DFS(nx, ny)

    for i in range(k):
        if i % 2 == 0:
            for j in range(m):
                if arr[n - spear[i]][j] == 'x':
                    arr[n - spear[i]][j] = '.'
                    for t in range(4):
                        can=False
                        nxx = n - spear[i] + dx[t]
                        nyy = j + dy[t]
                        if 0 <= nxx < n and 0 <= nyy < m and arr[nxx][nyy]=='x':
                            s = set()
                            l = set()
                            DFS(nxx, nyy)
                            for xx,yy in l:
                                visited[xx][yy]=False
                            if not can:
                                d = godown(s,l)
                                for z, x in l:
                                    arr[z][x] = '.'
                                for z, x in l:
                                    arr[z + d][x] = 'x'
                    break
        else:
            for j in range(m - 1, -1, -1):
                if arr[n - spear[i]][j] == 'x':
                    arr[n - spear[i]][j] = '.'
                    for t in range(4):
                        can=False
                        nxx = n - spear[i] + dx[t]
                        nyy = j + dy[t]
                        if 0 <= nxx < n and 0 <= nyy < m and arr[nxx][nyy]=='x':
                            s = set()
                            l = set()
                            DFS(nxx, nyy)
                            for xx,yy in l:
                                visited[xx][yy]=False
                            if not can:
                                d = godown(s,l)
                                for z, x in l:
                                    arr[z][x] = '.'
                                for z, x in l:
                                    arr[z + d][x] = 'x'
                    break
    for i in range(n):
        for j in range(m):
            print(arr[i][j],end='')
        print()


if __name__ == '__main__':
    n, m = map(int, input().split())
    visited = [[False] * m for _ in range(n)]
    arr = []
    for _ in range(n):
        arr.append(list(input().rstrip()))
    k = int(input())
    spear = list(map(int, input().split()))
    solution(arr, spear)
