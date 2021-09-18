import sys
input=sys.stdin.readline

def solution(arr):
    global answer,can
    def go(cnt):
        global answer,can
        for x in range(10):
            for y in range(10):
                if arr[x][y]:
                    for i in range(1,6):
                        #if i==5:
                        #    print(i,cnt,(x,y),paper)
                        #    for q in range(10):
                        #        print(arr[q])
                        if paper[i]<1:
                            continue
                        if checkCan(x,y,i) and arr[x][y]:
                            getcheck(i,x,y,True)
                            paper[i]-=1
                            go(cnt+1)
                            paper[i]+=1
                            getcheck(i,x,y,False)
                        else:
                            break
                    return
        can=True
        answer=min(answer,cnt)

    def checkCan(x,y,i):
        if x+i-1>=10 or y+i-1>=10:
            return False
        else:
            for m in range(x,x+i):
                for l in range(y,y+i):
                    if arr[m][l]==0:
                        return False
            return True


    def getcheck(n,x,y,what):
        for i in range(x,x+n):
            for j in range(y,y+n):
                if 0<=i<10 and 0<=j<10:
                    if what:
                        arr[i][j]=0
                    else:
                        arr[i][j] = 1

    answer=sys.maxsize
    paper=[5 for _ in range(6)]
    can=False
    go(0)
    if can:
        print(answer)
    else:
        print(-1)

if __name__ == '__main__':
    arr=[]
    for i in range(10):
        arr.append(list(map(int,input().split())))
    solution(arr)