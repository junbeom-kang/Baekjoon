import sys
from collections import defaultdict
input=sys.stdin.readline
def solution():
    n,p=map(int,input().split())
    where=[1 for _ in range(p+1)]
    item=[defaultdict(int) for _ in range(p+1)]
    log=[]
    ban=set()
    for i in range(n):
        temp=list(input().split())
        if temp[2]=='M':
            where[int(temp[1])]=int(temp[3])
        elif temp[2]=='F':
            item[int(temp[1])][int(temp[3])]+=1
            if int(temp[3])!=where[int(temp[1])]:
                log.append(int(temp[0]))
        elif temp[2]=='A':
            if where[int(temp[1])]!=where[int(temp[3])]:
                log.append(int(temp[0]))
                ban.add(int(temp[1]))
        else:
            if item[int(temp[1])][int(temp[3])]<1 or item[int(temp[1])][int(temp[4])]<1:
                log.append(int(temp[0]))
            if item[int(temp[1])][int(temp[3])]>0:
                item[int(temp[1])][int(temp[3])]-=1
            if item[int(temp[1])][int(temp[4])]>0:
                item[int(temp[1])][int(temp[4])]-=1

    print(len(log))
    if log:
        print(*log)
    ban=list(ban)
    ban.sort()
    print(len(ban))
    if ban:
        print(*ban)
    return

if __name__ == '__main__':
    solution()

