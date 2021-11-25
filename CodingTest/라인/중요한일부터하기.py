import sys
from collections import deque,defaultdict
input=sys.stdin.readline

def solution(jobs):
    temp=deque(jobs)
    answer=[]
    n=len(jobs)
    work=defaultdict(int)
    weight=defaultdict(int)
    last=temp[-1][0]
    start,time,now,w=temp.popleft()
    answer.append(now)
    end=time+start
    for i in range(last+1):
        if end<i:
            end=i
        #print(end)
        if temp[0][0]==i:
            start,time,num,w=temp.popleft()
            work[num]+=time
            if weight[num]:
                weight[num]=w
            else:
                if weight[num]<w:
                    weight[num]=w
        if i==end and weight:
            if weight[now]:
                del weight[now]
                end+=work[now]
                work[now]=0
            else:
                del weight[now]
                next=sorted(weight.items(),reverse=True,key=lambda x:(x[1],-x[0]))[0][0]
                answer.append(next)
                end+=work[next]
                work[next]=0
                del weight[next]
                now=next
    if weight:
        for i in sorted(weight.items(),reverse=True,key=lambda x:(x[1],-x[0])):
            answer.append(i[0])
    print(answer)
    return


if __name__ == '__main__':
    solution([[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]])
    solution([[1,2,1,5], [2,1,2,100], [3,2,1,5], [5, 2, 1, 5]])
    solution([[0,2,3,1], [5,3,3,1], [10,2,4,1]])