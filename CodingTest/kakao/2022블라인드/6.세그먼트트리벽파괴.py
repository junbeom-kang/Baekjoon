from math import ceil, log2


def solution(board, skill):
    global answer, tree
    answer=0
    m=len(board[0])
    n=len(board)
    size = 2 ** ceil(log2(n*m))
    tree = [0] * (2 * size)
    temp = 0
    for i in board:
        for j in i:
            tree[size + temp] = j
            temp += 1

    for query in skill:
        if query[0] == 1:
            for i in range(query[1],query[3]+1):
                plus(1, size, i*m+query[2]+1, i*m+query[4]+1, 1, -query[5])
        else:
            for i in range(query[1], query[3] + 1):
                plus(1, size, i * m + query[2]+1, i * m + query[4]+1, 1, query[5])
    for i in range(1,len(board) * len(board[0])+1):
        if find(size + i - 1) > 0:
            answer += 1

    return answer


def plus(start, end, left, right, node, diff):
    if right < start or left > end:
        return
    if left <= start and end <= right:
        tree[node] += diff
        return
    mid = (start + end) // 2
    plus(start, mid, left, right, 2 * node, diff)
    plus(mid + 1, end, left, right, 2 * node + 1, diff)


def find(node):
    ans = 0
    while node >= 1:
        ans += tree[node]
        node //= 2
    return ans


