import sys
from collections import deque
a,b=map(int,input().split())
check=[-1]*(100001)
check[a]=0
def bfs(a,b):
    Q=deque([a])
    cnt=1
    while Q:
        for _ in range(len(Q)):
            temp=Q.popleft()
            if temp+1<100001:
                if check[temp+1]==-1:
                    check[temp+1]=temp
                    if temp+1==b:
                        return cnt
                    Q.append(temp+1)
            if temp-1>=0:
                if check[temp-1]==-1:
                    check[temp-1]=temp
                    if temp-1==b:
                        return cnt
                    Q.append(temp-1)
            if 2*temp<100001:
                if check[2*temp]==-1:
                    check[2*temp]=temp
                    if temp*2==b:
                        return cnt
                    Q.append(2*temp)
        cnt+=1

if a==b:
    print(0)
    print(a)
else:
    temp=bfs(a,b)
    print(temp)
    ans=[b]
    while check[b]!=a:
        ans.append(check[b])
        b=check[b]
    ans.append(a)
    print(*ans[::-1])
