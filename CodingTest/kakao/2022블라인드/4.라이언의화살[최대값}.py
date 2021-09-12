from copy import deepcopy
def solution(n, info):
    global answer,answerList
    answerList=[]
    answer=-1000000
    end=len(info)
    temp=[0]*11
    go(n,0,end,info,0,temp)
    if answer<=0:
        return [-1]
    else:
        return answerList

def go(n,start,end,info,cnt,list):
    global answer,answerList
    if start>=11 or cnt>n:
        return
    if cnt==n:
        she=0
        sum=0
        for i in range(11):
            if info[i]>=list[i] and info[i]>0:
                she+=(10-i)
            elif list[i]>info[i]:
                sum+=(10-i)
        if sum-she>=answer:
            if answer==(sum-she):
                for i in range(10,-1,-1):
                    if answerList[i]>list[i]:
                        break
                    elif list[i]>answerList[i]:
                        answerList = deepcopy(list)
                        break
            else:
                answer=sum-she
                answerList=deepcopy(list)

    else:
        go(n,start+1,end,info,cnt,list)
        list[start]+=1
        go(n,start,end,info,cnt+1,list)
        list[start]-=1





print(solution(1,[1,0,0,0,0,0,0,0,0,0,0]))