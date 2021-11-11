import sys
from collections import deque
input=sys.stdin.readline

def solution():
    can=False
    f,s,g,u,d=map(int,input().split())
    Q=deque([])
    visited=[False]*(f+1)
    Q.append(s)
    visited[s]=True
    cnt=0
    while Q:
        lq=len(Q)
        for i in range(lq):
            t=Q.popleft()
            if t==g:
                can=True
                Q=[]
                break
            if t+u<=f and not visited[t+u]:
                visited[t+u]=True
                Q.append(t+u)
            if t-d>=1 and not visited[t-d]:
                visited[t-d]=True
                Q.append(t-d)
        cnt+=1
    if can:
        print(cnt-1)
    else:
        print("use the stairs")


    return

if __name__ == '__main__':
    solution()

