from itertools import combinations
def solution(needs, r):
    def check(nums):
        tt=0
        for i in range(n):
            tempt=0
            for t in nums:
                if needs[i][t]==1:
                    tempt+=1
            if numindex[i]==tempt:
                tt+=1
        return tt

    answer = 0
    n=len(needs)
    m=len(needs[0])
    numindex=[]
    for i in range(n):
        tt=0
        for j in range(m):
            if needs[i][j]==1:
                tt+=1
        numindex.append(tt)
    temp=[i for i in range(m)]
    for i in combinations(temp,r):
        answer=max(answer,check(i))
    print(answer)
    return answer
#solution([ [ 1, 0, 0 ], [1, 1, 0], [1, 1, 0], [1, 0, 1], [1, 1, 0], [0, 1, 1] ],2)
solution([[0,0], [0,0]], 1)