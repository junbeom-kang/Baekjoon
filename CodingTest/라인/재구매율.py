import sys
from collections import defaultdict
input=sys.stdin.readline

def solution(records,k,date):
    def check(s,date):
        y1,m1,d1=map(int,s.split('-'))
        tt=3600*y1+30*m1+d1
        return date-tt

    y,m,d=map(int,date.split('-'))
    date=3600*y+30*m+d
    start=0
    n=len(records)
    arr=[]
    answer=[]
    for i in range(n):
        arr.append(list(records[i].split()))
    end=n
    canA,canB=False,False
    for i in range(n):
        if check(arr[i][0],date-k+1)<=0:
            start=i
            canA=True
            break
    for i in range(n-1,-1,-1):
        if check(arr[i][0],date)>=0:
            end=i+1
            canB=True
            break
    realanswer = []
    if canA and canB:
        item=set()
        for i in range(start,end):
            item.add(arr[i][2])
        for i in item:
            temp=defaultdict(int)
            for j in range(start,end):
                if arr[j][2]==i:
                    temp[arr[j][1]]+=1
            re=0
            sum=0
            for t in temp.keys():
                if temp[t]>1:
                    re+=1
                sum+=temp[t]
            answer.append([re/len(temp),sum,i])

        for i in sorted(answer,reverse=True,key=lambda x:(x[0],x[1],x[2])):
            realanswer.append(i[2])
    else:
        realanswer.append("no result")
    print(realanswer)


if __name__ == '__main__':
    solution(["2020-02-02 uid1 pid1","2020-02-26 uid1 pid1","2020-02-26 uid2 pid1","2020-02-27 uid3 pid2",
              "2020-02-28 uid4 pid2","2020-02-29 uid3 pid3","2020-03-01 uid4 pid3","2020-03-03 uid1 pid1",
              "2020-03-04 uid2 pid1","2020-03-05 uid3 pid2","2020-03-05 uid3 pid3","2020-03-05 uid3 pid3",
              "2020-03-06 uid1 pid4"],10,"2020-03-05")
    #solution(["2020-02-02 uid141 pid141","2020-02-03 uid141 pid32","2020-02-04 uid32 pid32","2020-02-05 uid32 pid141"], 10, "2020-02-05")
    #solution(["2020-01-01 uid1000 pid1000"], 10, "2020-01-11")

