import sys
from collections import deque
input=sys.stdin.readline

def solution():
    n,q,c=map(int,input().split())
    size=[0]
    size.extend(list(map(int,input().split())))
    b,f=deque([]),deque([])
    bs,fs,cur=0,0,0
    for i in range(q):
        t=input().split()
        if t[0]=='B' and b:
            f.appendleft(cur)
            fs+=size[cur]
            cur=b.pop()
            bs-=size[cur]
        elif t[0]=='F' and f:
            b.append(cur)
            bs+=size[cur]
            cur=f.popleft()
            fs-=size[cur]
        elif t[0]=='A':
            if cur:
                temp=bs+size[cur]+size[int(t[1])]
                while temp>c:
                    tt=size[b.popleft()]
                    temp-=tt
                    bs-=tt
                f=deque([])
                fs=0
                b.append(cur)
                bs+=size[cur]
                cur=int(t[1])
            else:
                cur=int(t[1])
        elif t[0]=='C' and len(b)>1:
            temp=deque([b[0]])
            lb=len(b)
            j=1
            while j<lb:
                if b[j]==b[j-1]:
                    if temp[-1]!=b[j]:
                        temp.append(b[j])
                    bs -= size[b[j]]
                else:
                    temp.append(b[j])
                j+=1

            b=temp
    print(cur,f,fs,b,bs)
    print(cur)
    if b:
        for i in range(len(b)-1,-1,-1):
            print(b[i],end=' ')
        print()
    else:
        print(-1)
    if not f:
        print(-1)
    else:
        print(*f)
    return

if __name__ == '__main__':
    solution()

