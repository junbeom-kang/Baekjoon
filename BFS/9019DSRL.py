import sys
from collections import deque

def bfs(a,b):
    visited=[-1]*10000
    L=[]
    visited[a]=0
    Q=deque([a])
    while Q:
        temp=Q.popleft()
        if temp==b:
            while visited[temp]!=0:
                L.append(visited[temp][1])
                temp=visited[temp][0]
            return L
        d=(temp*2)%10000
        if visited[d]==-1:
            visited[d]=(temp,'D')
            Q.append(d)
        s=temp-1
        if s==-1:
            s=9999
        if visited[s]==-1:
            visited[s]=(temp,'S')
            Q.append(s)
        l=(temp//1000)+10*(temp%1000)
        if visited[l]==-1:
            visited[l]=(temp,'L')
            Q.append(l)
        r=(temp//10)+1000*(temp%10)
        if visited[r]==-1:
            visited[r]=(temp,'R')
            Q.append(r)


input=sys.stdin.readline
T=int(input())
for _ in range(T):
    a,b=map(int,input().split())
    ans=bfs(a,b)
    for i in ans[::-1]:
        print(i,end='')
    print()