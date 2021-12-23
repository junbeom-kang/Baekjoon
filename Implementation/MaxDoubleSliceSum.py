import sys
input=sys.stdin.readline

def solution(A):
    l=len(A)
    left=[0]*l
    right=[0]*l
    for i in range(1,l-1):
        if left[i-1]<0:
            left[i]=A[i]
        else:
            left[i]=left[i-1]+A[i]
    for i in range(l-2,0,-1):
        if right[i+1]<0:
            right[i]=A[i]
        else:
            right[i]=right[i+1]+A[i]
    answer=0
    for i in range(1,l-1):
        if left[i-1]>0 and right[i+1]<0:
            answer = max(answer, left[i - 1])
        elif left[i-1]<0 and right[i+1]>0:
            answer = max(answer, right[i + 1])
        else:
            answer=max(answer,left[i-1]+right[i+1])

    return answer

if __name__ == '__main__':
    #solution([1,2,3,4])
    answer=[]
    for i in range(-10,11):
        answer.append(i)
    solution(answer)
    #solution([-3, -2, -6, -1, 6, -12, -1, -3])


