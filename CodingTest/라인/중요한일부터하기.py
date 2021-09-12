
from collections import defaultdict
def solution(jobs):
    dic=defaultdict(int)
    l=len(jobs)
    index=1
    start,end,num,weight=jobs[0]
    now=num
    while jobs[index][0]<=start+end:
        if jobs[index][2]==num:
            end+=jobs[index][1]
        else:
            dic[jobs[index][2]]+=jobs[index][3]
    sorted(dic.items(),reverse=True,key=lambda item:item[1])
    sorted(dic.keys(),reverse=True)




    return answer

if __name__ == '__main__':
    solution([[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]])