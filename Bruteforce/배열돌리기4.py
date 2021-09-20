import sys
from itertools import permutations
from copy import deepcopy
input = sys.stdin.readline


def solution(n,m,k,Arr,spin):
    def turn(x,y,t):
        for i in range(1,t+1):
            temp=arr[x-i][y-i]
            for a in range(x-i,x+i):
                arr[a][y-i]=arr[a+1][y-i]
            for b in range(y - i, y + i):
                arr[x+i][b] = arr[x+i][b+1]
            for c in range(x + i, x - i,-1):
                arr[c][y + i] = arr[c - 1][y + i]
            for d in range(y + i, y - i,-1):
                arr[x-i][d] = arr[x-i][d-1]

            arr[x-i][y-i+1]=temp

    def cal(copyArr):
        r=sys.maxsize
        for i in range(n):
            r=min(r,sum(copyArr[i]))
        return r

    answer=sys.maxsize
    for z in permutations(spin,k):
        arr=deepcopy(Arr)
        for t,y,u in z:
            turn(t-1,y-1,u)

        answer=min(answer,cal(arr))
    print(answer)



if __name__ == '__main__':
    n,m,k=map(int,input().split())
    Arr=[]
    for i in range(n):
        Arr.append(list(map(int,input().split())))
    spin=[]
    for i in range(k):
        spin.append(list(map(int,input().split())))
    solution(n,m,k,Arr,spin)