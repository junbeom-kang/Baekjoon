import sys
input=sys.stdin.readline

def solution(data):
    global realAnswer
    realAnswer=0
    def start(data,n,sum):
        global answer,realAnswer
        if n==10:
            realAnswer=max(realAnswer,sum)
        else:
            for i in range(4):
                if now[i]==21:
                    continue
                temp=go(now[i],data[n])
                if temp!=-1:
                    before=now[i]
                    now[i]=temp
                    start(data,n+1,sum+num[temp])
                    now[i]=before

    def check(v):
        if v in now and v!=21:
            return False
        else:
            return True
    def go(v,cnt):
        if v in blue:
            if cnt>=2:
                return go(blue[v],cnt-1)
            else:
                if not check(blue[v]):
                    return -1
                else:
                    return blue[v]
        else:
            while cnt>0:
                v=arr[v]
                cnt-=1
            if check(v):
                return v
            else:
                return -1
    num=[]
    for i in range(21):
        num.append(i*2)
    num.extend([0,13,16,19,25,22,24,28,27,26,30,35])
    arr=[]
    for i in range(21):
        arr.append(i+1)
    arr.append(21)
    arr.extend([23,24,25,31,27,25,29,30,25,32,20])
    blue={5:22,10:26,15:28}
    now=[0,0,0,0]

    checked=[0]*33
    start(data,0,0)
    print(realAnswer)





if __name__ == '__main__':
    data=list(map(int,input().split()))
    solution(data)