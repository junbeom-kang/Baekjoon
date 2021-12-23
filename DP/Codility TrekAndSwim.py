import sys
input=sys.stdin.readline

def solution(A):
    def doLeft(v):
        res=0
        temp=0
        sum=0
        for i in range(v,-1,-1):
            if not A[i]:
                temp-=1
            else:
                temp+=1
            sum+=1
            if temp<0:
                res=sum
        return res
    def doRight(v):
        res=0
        temp=0
        sum=0
        for i in range(v,l):
            if not A[i]:
                temp-=1
            else:
                temp+=1
            sum+=1
            if temp>0:
                res=sum
        return res

    answer=0
    l=len(A)
    left=[0]*l
    right=[0]*l
    for i in range(l-1):
        left[i]=doLeft(i)
        right[i+1]=doRight(i+1)
    print(left)
    print(right)
    for i in range(1,l-1):
        answer=max(answer,left[i]+right[i+1])
        print(answer)
    print(answer)
    return

if __name__ == '__main__':
    solution([0,1,1,1])

