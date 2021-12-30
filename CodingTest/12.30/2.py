import sys
input=sys.stdin.readline
from collections import deque
from copy import deepcopy
def solution(stones, k):
    answer =[]
    n=len(stones)
    Q=deque()
    Q.append([stones,[]])
    can=True
    while can and Q:
        lq=len(Q)
        for _ in range(lq):
            temp,l=Q.popleft()
            print(temp,l,"!!")
            for i in range(n):
                smallCan=False
                newTemp=deepcopy(temp)
                for j in range(n):
                    if j!=i and newTemp[j]==0:
                        smallCan=True
                        break
                    newTemp[j]-=1
                if smallCan:
                    break
                newTemp[i]+=2
                l.append(i)
                nt = deepcopy(l)
                if sum(newTemp)==k and newTemp[i]==k:
                    answer.append(nt)
                    can=False
                else:
                    Q.append([newTemp,nt])
                l.pop()
    answer.sort()
    return (''.join(map(str, answer[-1])))


if __name__ == '__main__':
    solution([1, 3, 2],3)

