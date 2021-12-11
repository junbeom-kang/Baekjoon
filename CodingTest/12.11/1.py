def solution(arr):
    answer = 0
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
        if sum>0:
            answer+=1
    print(answer)
    return answer

solution([ 5, -5, -16, 4 ])