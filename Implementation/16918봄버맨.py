import sys

input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def solution(n, m, c, arr):
    if c % 2 == 0:
        answer=[['O']*m for _ in range(n)]
        for i in range(n):
            print(''.join(answer[i]))
    elif c==1:
        for i in range(n):
            print(''.join(arr[i]))

    else:
        all = set()
        now = set()
        for i in range(n):
            for j in range(m):
                all.add((i, j))
                if arr[i][j] == 'O':
                    now.add((i, j))
        temp = set()
        for x, y in now:
            temp.add((x,y))
            for t in range(4):
                nx = x + dx[t]
                ny = y + dy[t]
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in now:
                    temp.add((nx, ny))
        temp = all - temp
        now=set()
        for x, y in temp:
            now.add((x,y))
            for t in range(4):
                nx = x + dx[t]
                ny = y + dy[t]
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in temp:
                    now.add((nx, ny))
        now=all-now
        answer = [['.'] * m for _ in range(n)]
        if c%4==1:
            for x, y in now:
                answer[x][y] ='O'
        else:
            for x,y in temp:
                answer[x][y]='O'
        for i in range(n):
            print(''.join(answer[i]))



if __name__ == '__main__':
    n, m, c = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(input().rstrip()))

    solution(n, m, c, arr)
