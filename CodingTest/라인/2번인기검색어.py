from collections import defaultdict
from copy import deepcopy
def solution(research, n, k):
    global dic
    dic=defaultdict(int)
    l=len(research)
    if l-n<0:
        return None
    for i in range(l-n+1):
        cal(i,i+n-1,research,n,k)
    if len(dic)==0:
        return "None"
    else:
        dic=sorted(dic.items(),key=lambda x:(-x[1],x[0]))
        return str(dic[0][0])


def cal(start,end,research,n,k):
    global dic
    temp=""
    setList=set(research[start])
    copyset=deepcopy(setList)
    for j in range(start,end+1):
        temp+=research[j]
    for t in copyset:
        for i in range(start,end+1):
            if research[i].count(t)<k:
                print(research[i])
                print(research[i].count(t))
                print(t)
                setList.remove(t)
                break
    print(dic)
    for t in setList:
        if temp.count(t)>=(2*n*k):
            dic[t]+=1

if __name__ == '__main__':
    print(solution(		["yxxy", "xxyyy"], 2, 1))