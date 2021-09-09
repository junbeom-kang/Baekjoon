import sys
def solution(stones, k):
    global answer
    answer=-1
    bs(0,sys.maxsize,stones,k)
    return answer+1


def bs(start,end,stones,k):
    global answer
    while start<=end:
        mid=(start+end)//2
        if check(mid,stones,k):
            answer=mid
            start=mid+1
        else:
            end=mid-1

def check(minus,stones,k):
    i=-1
    l=len(stones)
    while i<l:
        can=False
        for j in range(1,k+1):
            if i+j>=l:
                can=True
                i+=j
                break
            if stones[i+j]-minus>0:
                can=True
                i+=j
                break
        if not can:
            return False
    if i>=l:
        return True
    else:
        return False


if __name__ == '__main__':
    print(solution( [2, 4, 5, 3, 2, 1, 4, 2, 5, 1],	3))