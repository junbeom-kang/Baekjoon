import sys
from collections import deque
input=sys.stdin.readline
def push(l,w):
    global ans
    t=[]
    c=0
    while c<len(l):
        if c==len(l)-1:
            t.append(l[c])
        elif l[c]==l[c+1]:
            t.append(l[c]*2)
            c+=1
        else:
            t.append(l[c])
        c+=1
    if t:
        ans=max(ans,max(t))
    if w=='r':
        return t+[0]*(n-len(t))
    else:
        return [0]*(n-len(t))+t[::-1]

def move(arr):
    h,v=[[]for _ in range(n)],[[]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j]!=0:
                h[i].append(arr[i][j])
            if arr[j][i]!=0:
                v[i].append(arr[j][i])
    h1,h2,v1,v2=[],[],[],[]
    for i in range(n):
        h1.append(push(h[i],'r'))
        h2.append(push(h[i][::-1],'l'))
        v1.append(push(v[i],'r'))
        v2.append(push(v[i][::-1],'l'))
    V1=[[]for _ in range(n)]
    V2=[[]for _ in range(n)]
    for p in range(n):
        for pp in range(n):
            V1[pp].append(v1[p][pp])
    for p in range(n):
        for pp in range(n):
            V2[pp].append(v2[p][pp])
    return h1,h2,V1,V2

n=int(input())
adj=[list(map(int,input().split())) for _ in range(n)]
count=0
Q=deque([adj])
ans=0
while Q:
    if count==5:
        break
    for _ in range(len(Q)):
        temp=Q.popleft()
        q,w,e,r=move(temp)
        Q.extend([q,w,e,r])
    count+=1
print(ans)
