import sys
input=sys.stdin.readline
#탈출조건

def solution(n,num,weight):
    def go(v,cnt):
        global answer
        if v==n:
            answer=max(answer,cnt)
            return
        if num[v]<=0:
            go(v+1,cnt)
            return

        else:
            for i in range(n):
                if i==v:continue
                temp=0
                if num[i]>0:
                    num[i]-=weight[v]
                    if num[i]<=0:
                        temp+=1
                    num[v]-=weight[i]
                    if num[v]<=0:
                        temp+=1

                    go(v+1,cnt+temp)
                    num[i]+=weight[v]
                    num[v]+=weight[i]
            if v==n-1:
                go(v+1,cnt)
    go(0,0)
    print(answer)

answer=0
n=int(input())
num=[0]*n
weight=[0]*n
for i in range(n):
    num[i],weight[i]=map(int,input().split())
solution(n,num,weight)