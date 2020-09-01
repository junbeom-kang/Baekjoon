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
                    check[temp+1]=cnt
                    if temp+1==b:
                        return check[b]
                    Q.append(temp+1)
            if temp-1>=0:
                if check[temp-1]==-1:
                    check[temp-1]=cnt
                    if temp-1==b:
                        return check[b]
                    Q.append(temp-1)
            if 2*temp<100001:
                if check[2*temp]==-1:
                    check[2*temp]=cnt
                    if temp*2==b:
                        return check[b]
                    Q.append(2*temp)
        cnt+=1
def reversebfs(b,a):
    ans=[b]
    Q=deque([b])
    cnt=check[b]
    while Q:
        for _ in range(len(Q)):
            temp=Q.popleft()
            if temp==a:
                return ans
            if temp%2==0:
                if check[temp//2]==cnt-1:
                    Q.append(temp//2)
                    ans.append(temp//2)
                    break
            if temp+1<=100000:
                if check[temp+1]==cnt-1:
                    Q.append(temp+1)
                    ans.append(temp+1)
                    break
            if temp-1>=0:
                if check[temp-1]==cnt-1:
                    Q.append(temp-1)
                    ans.append(temp-1)
                    break
        cnt-=1
if a==b:
    print(0)
    print(a)
else:
    print(bfs(a,b))
    print(*reversebfs(b,a)[::-1])