from math import ceil, sqrt
def solution(n, m):
    if n<=2:
        print(2)
    if n==1:
        n+=1
    for i in range(n, m + 1):
        can = False
        for j in range(2, ceil(sqrt(i))+1):
            if (i % j) == 0:
                can = True
                break
        if not can:
            print(i)
n,m=map(int,input().split())
solution(n,m)