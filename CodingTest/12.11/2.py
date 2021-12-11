from heapq import heappush,heappop
from math import dist,ceil
def solution(x, y):
    global cnt
    def find(v):
        if parent[v] == v:
            return v
        else:
            parent[v] = find(parent[v])
            return parent[v]

    def merge(a, b):
        global cnt
        x = find(a)
        y = find(b)
        if x == y:
            return
        else:
            cnt+=1
            if x < y:
                parent[y] = x
            else:
                parent[x] = y

    n=len(x)
    parent=[i for i in range(n)]
    Q=[]
    for i in range(n-1):
        for j in range(i+1,n):
            heappush(Q,[dist((x[i],y[i]),(x[j],y[j])),i,j])
    cnt=0
    while cnt<n-1:
        l,x,y=heappop(Q)
        merge(x,y)
        answer=l
    answer=ceil(answer)
    print(answer)
    return answer

solution([1, 2, 6, 8],[1, 2, 5, 7])
solution([1, 2, 4, 2],[1, 1, 4, 2]	)