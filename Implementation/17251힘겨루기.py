import sys
from heapq import heappush,heappop
input=sys.stdin.readline

def solution():
    n=int(input())
    temp=list(map(int,input().split()))
    red=[]
    blue=[]
    Rq=[]
    Bq=[]
    r,b=0,0
    for i in range(n-1):
        heappush(Rq,-temp[i])
        red.append(-Rq[0])
    for i in range(n-1,0,-1):
        heappush(Bq,-temp[i])
        blue.append(-Bq[0])
    blue=blue[::-1]
    for i in range(len(blue)):
        if red[i]>blue[i]:
            r+=1
        elif red[i]<blue[i]:
            b+=1
    if r>b:
        print('R')
    elif r==b:
        print('X')
    else:
        print('B')

    return

if __name__ == '__main__':
    solution()

