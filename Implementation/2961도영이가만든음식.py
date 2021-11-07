import sys
input=sys.stdin.readline

def solution():
    global answer,sx
    def check(temp):
        global answer
        first=1
        second=0
        for i in range(n):
            if temp&(1<<i):
                first*=arr[i][0]
                second+=arr[i][1]
        answer=min(answer,abs(first-second))


    def start(num,cnt):
        if cnt==n:
            if num:
                check(num)
            return
        start(num, cnt + 1)
        start(num+(1<<cnt),cnt+1)

    answer = sys.maxsize
    n=int(input())
    arr=[]
    for i in range(n):
        q,w=map(int,input().split())
        arr.append([q,w])
    sx=0
    start(0,0)
    print(answer)
    return

if __name__ == '__main__':
    solution()

