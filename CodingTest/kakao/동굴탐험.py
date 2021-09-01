import sys
sys.setrecursionlimit(10**9)

def solution(n, path, order):
    global temp, arr, check, pre_visit
    answer = True
    pre_visit = [0] * n
    temp = [0 for _ in range(n)]
    arr = [[] for _ in range(n)]
    check = [False] * n
    for i in path:
        arr[i[0]].append(i[1])
        arr[i[1]].append(i[0])

    for i in order:
        pre_visit[i[1]] = i[0]
    if pre_visit[0]!=0:
        answer=False
    else:
        start(0)
        for i in range(n):
            if not check[i]:
                answer = False
                break

    return answer


def start(v):
    check[v] = True
    if temp[v] != 0:
        start(temp[v])
    for i in arr[v]:
        if check[i]:
            continue
        if not check[pre_visit[i]]:
            temp[pre_visit[i]] = i
            continue
        start(i)


if __name__ == '__main__':
    print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],[[4,1],[8,7],[6,5]]))
