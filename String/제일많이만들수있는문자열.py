import sys
from collections import defaultdict
input=sys.stdin.readline

def solution(S,L):
    temp=defaultdict(int)
    answer=0
    for i in S:
        temp[i]+=1
    for i in L:
        minvalue=sys.maxsize
        pd=defaultdict(int)
        for j in i:
            pd[j]+=1
        for t in pd.keys():
            minvalue=min(minvalue,temp[t]//pd[j])
            if minvalue==0:
                break
        answer=max(answer,minvalue)
        print(answer)
    print(answer)

    return

if __name__ == '__main__':
    S="LILLYBILLYOO"
    L=["BBILL", "MARIA", "LILLY"]
    solution(S,L)

