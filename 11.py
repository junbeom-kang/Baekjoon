import sys
from itertools import combinations
input=sys.stdin.readline
ans=0
n,k=map(int,input().split())
if k>5:
    data=[]
    for i in range(n):
        temp=[]
        for e in input().rstrip()[4:-4]:
            if e=='a'or e=='n' or e==' t'or e=='i' or e=='c':
                continue
            temp.append(ord(e)-ord('a'))
        data.append(temp)
    num=[i for i in range(26)]
    num.remove(ord('a')-ord('a'))
    num.remove(ord('n')-ord('a'))
    num.remove(ord('t')-ord('a'))
    num.remove(ord('i')-ord('a'))
    num.remove(ord('c')-ord('a'))
    temp=0
    temp|=1<<(ord('a')-ord('a'))
    temp|=1<<(ord('n')-ord('a'))
    temp|=1<<(ord('t')-ord('a'))
    temp|=1<<(ord('i')-ord('a'))
    temp|=1<<(ord('c')-ord('a'))
    for i in combinations(num,k-5):
        t=temp
        cnt=0
        for j in i:
            if not t&(1<<j):
                t|=1<<j
        for d in data:
            can=True
            for q in d:
                if not t&(1<<q):
                    can=False
                    break
            if can:
                cnt+=1
        ans=max(ans,cnt)
    print(ans)
elif k==5:
    ans=0
    data=[]
    for i in range(n):
        temp=[]
        for e in input().rstrip()[4:-4]:
            if e=='a'or e=='n' or e=='t'or e=='i' or e=='c':
                continue
            temp.append(ord(e)-ord('a'))
        data.append(temp)
    temp = 0
    temp |= 1 << (ord('a') - ord('a'))
    temp |= 1 << (ord('n') - ord('a'))
    temp |= 1 << (ord('t') - ord('a'))
    temp |= 1 << (ord('i') - ord('a'))
    temp |= 1 << (ord('c') - ord('a'))
    for i in data:
        can=True
        for r in i:
            if not temp&(1<<r):
                can=False
        if can:
            ans+=1
    print(ans)



else:
    print(0)