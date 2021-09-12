from math import ceil
from collections import defaultdict
def solution(fees, records):
    normalTime=fees[0]
    normalFee=fees[1]
    plusTime=fees[2]
    plusFee=fees[3]
    fees=defaultdict(int)
    Indict={}
    for i in records:
        time,num,what=i.split()
        if what=="IN":
            Indict[num]=time
        else:
            fees[num]+=(change(time)-change(Indict[num]))
            del Indict[num]
    for i in Indict.keys():
        fees[i]+=change("23:59")-change(Indict[i])
    answerdic={}
    for i in fees:
        answerdic[i]=getCharge(fees[i], normalTime, normalFee, plusTime, plusFee)
    answerlist=sorted(answerdic)
    answer = []
    for i in answerlist:
        answer.append(answerdic[i])
    return answer
def change(time):
    hour,min=list(map(int,time.split(":")))
    return hour*60+min
def getCharge(min,normaltime,normalfee,plustime,plusFee):
    if min<=normaltime:
        return normalfee
    else:
        return normalfee+ceil((min-normaltime)/plustime)*plusFee



if __name__ == '__main__':
    print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))