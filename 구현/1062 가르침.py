import sys
from itertools import combinations
input=sys.stdin.readline
def change(temp):
    res=[]
    for i in temp:
        res.append(ord(i)-ord('a'))
    return res

ans=0
poss=0
n,k=map(int,input().split())
if k>=5:
    num=set()
    data=[]
    for i in range(n):
        t=change(set(input().rstrip()[4:-4])-set(['a','n','i','t','c']))
        if len(t)==0:
            poss+=1
            continue
        num|=set(t)
        data.append(t)
    for i,r in enumerate(data):
        q=0
        for a in r:
            q|=(1<<a)
        data[i]=q
    temp=0
    temp|=1<<(ord('a')-ord('a'))
    temp|=1<<(ord('n')-ord('a'))
    temp|=1<<(ord('t')-ord('a'))
    temp|=1<<(ord('i')-ord('a'))
    temp|=1<<(ord('c')-ord('a'))
    if len(num)<k-5:
        print(n)
    else:
        for i in combinations(num,k-5):
            t=temp
            cnt=0
            for j in i:
                if not t&(1<<j):
                    t|=1<<j
            t^=(1<<26)-1
            for d in data:
                if d&t==0:
                    cnt+=1
            ans=max(ans,cnt)
        print(ans+poss)
else:
    print(0)