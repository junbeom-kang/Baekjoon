import sys
input=sys.stdin.readline

def solution(schedule):
    global answer
    def getdate(day):
        if day=="MO":
            return 0
        elif day=="TU":
            return 1
        elif day=="WE":
            return 2
        elif day=="TH":
            return 3
        else :
            return 4
    def setCheck(time,long):
        h,m=list(map(int,time.split(":")))
        num=((h-9)*2)+(m//30)
        ts=[]
        for i in range(num,num+long):
            ts.append(i)
        return ts



    def change(time):
        if len(time)>10:
            time=time.split(" ")
            D1,T1=time[0],time[1]
            D2,T2=time[2],time[3]
            f1=setCheck(T1,4)
            f2=setCheck(T2,4)
            d1=getdate(D1)
            d2=getdate(D2)
            for i in range(f1[0],f1[0]+4):
                if arr[d1][i]:
                    return False
            for i in range(f2[0],f2[0]+4):
                if arr[d2][i]:
                    return False
            return [d1,f1[0],d2,f2[0]]
        else:
            D1,T1=time.split(" ")
            f1=setCheck(T1,7)
            d1=getdate(D1)
            for i in range(f1[0],f1[0]+7):
                if arr[d1][i]:
                    return False
            return [d1,f1[0]]


    def do(v,cnt):
        global answer
        if cnt==5:
            answer+=1
            return
        else:
            for i in range(4):
                temp=change(schedule[v][i])
                if temp:
                    if len(temp)==2:
                        start=temp[1]+1
                        for i in range(5):
                            arr[temp[0]][start+i]=True
                        do(v + 1, cnt + 1)
                        for i in range(5):
                            arr[temp[0]][start+i]=False
                    else:
                        start1=temp[1]+1
                        start2=temp[3]+1
                        for i in range(2):
                            arr[temp[0]][start1 + i] = True
                            arr[temp[2]][start2 + i] = True
                        do(v + 1, cnt + 1)
                        for i in range(2):
                            arr[temp[0]][start1 + i] = False
                            arr[temp[2]][start2 + i] = False



    arr=[[False]*30 for _ in range(5)]
    answer = 0
    do(0,0)
    print(answer)
    return answer


if __name__ == '__main__':
    solution([["MO 12:00 WE 14:30", "MO 12:00", "MO 15:00", "MO 18:00"], ["TU 09:00", "TU 10:00", "TU 15:00", "TU 18:00"], ["WE 09:00", "WE 12:00", "WE 15:00", "WE 18:00"], ["TH 09:30", "TH 11:30", "TH 15:00", "TH 18:00"], ["FR 15:00", "FR 15:00", "FR 15:00", "FR 15:00"]])

