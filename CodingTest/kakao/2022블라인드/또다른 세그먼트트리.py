from math import ceil, log2


def solution(board, skill):
    global answer, tree,size,changeToArr
    answer=0
    m=len(board[0])
    n=len(board)
    size=n*m
    tree = [0] * ((m*n)+1)
    changeToArr=[]

    for i in board:
        for j in i:
            changeToArr.append(j)

    for query in skill:
        if query[0] == 1:
            for i in range(query[1],query[3]+1):
                plus(i*m+query[2]+1,-query[5])
                if (i*m+query[4]+1)<size:
                    plus(i*m+query[4]+2,query[5])
        else:
            for i in range(query[1], query[3] + 1):
                plus(i * m + query[2] + 1, query[5])
                if (i*m+query[4]+1)<size:
                    plus(i*m+query[4]+2,-query[5])

    for i in range(1,len(board) * len(board[0])+1):
        if find(i) > 0:
            answer += 1
    return answer


def plus(start,diff):
    while start <size + 1:
        tree[start]+=diff
        start+=start&-start


def find(node):
    temp=changeToArr[node-1]
    while node > 0:
        temp += tree[node]
        node-=node&-node
    return temp

if __name__ == '__main__':
    solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])
