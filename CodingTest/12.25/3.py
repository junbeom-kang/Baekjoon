import sys
input=sys.stdin.readline

from collections import Counter,deque


def solution(A):
    n=len(A)
    a=Counter(A)
    Q=deque([])
    answer = 0
    for i in range(1,n+1):
        if a[i]>=2:
            Q.extend([i]*(a[i]-1))

    for i in range(1,n+1):
        if not a[i]:
            answer+=abs(Q.popleft()-i)
            if answer>1000000000:
                answer=-1
                break
    return answer

if __name__ == '__main__':
    temp=[1]*200000
    print(solution(temp))
    tt=[]
    for i in range(1,200001):
        tt.append(i)
    print(sum(tt)-200000)


