import sys
from copy import deepcopy
input=sys.stdin.readline

def solution():
    answer=sys.maxsize
    temp=deepcopy(first)
    cnt=1
    temp[0]=temp[0]^1
    temp[1]=temp[1]^1
    for i in range(1,n-1):
        if second[i-1]!=temp[i-1]:
            temp[i-1]^=1
            temp[i]^=1
            temp[i+1]^=1
            cnt+=1
    if second[n-2]!=temp[n-2]:
        temp[n-2]^=1
        temp[n-1]^=1
        cnt+=1
    if temp[n-1]==second[n-1]:
        answer=min(answer,cnt)
    temp=deepcopy(first)
    cnt=0
    for i in range(1,n-1):
        if second[i-1]!=temp[i-1]:
            temp[i-1]^=1
            temp[i]^=1
            temp[i+1]^=1
            cnt+=1
    if second[n-2]!=temp[n-2]:
        temp[n-2]^=1
        temp[n-1]^=1
        cnt+=1
    if temp[n-1]==second[n-1]:
        answer=min(answer,cnt)
    if answer==sys.maxsize:
        print(-1)
    else:
        print(answer)
    return

if __name__ == '__main__':
    n=int(input())
    first=list(map(int,input().rstrip()))
    second=list(map(int,input().rstrip()))
    solution()
