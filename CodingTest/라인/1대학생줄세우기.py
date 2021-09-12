def solution(student, k):
    global answer
    answer=0
    index=[]
    for i,v in enumerate(student):
        if v==1:
            index.append(i)
    for i in range(len(index)-k+1):
        go(index[i],index[i+k-1],student)
    return answer

def go(start,end,student):
    global answer
    left=0
    right=0
    while start-1>=0:
        if student[start-1]==1:
            break
        else:
            left+=1
            start-=1
    while end+1<len(student):
        if student[end+1]==1:
            break
        else:
            end+=1
            right+=1
    answer+=((left+1)*(right+1))




if __name__ == '__main__':
    print(solution([0,1,0,0],100))