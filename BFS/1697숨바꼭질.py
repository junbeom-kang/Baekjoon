import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
ans=0
queue=deque([])
stack=[0]*100001
check=[False]*100001
queue.append(n)
while queue:
    for _ in range(len(queue)):
        temp=queue.popleft()
        if temp==m:
            print(ans)
            sys.exit()
        stack[temp]=1
        check[temp]=True
        if temp+1<100001 and not check[temp+1]:
            queue.append(temp+1)
        if temp-1>=0 and not check[temp-1]:
            queue.append(temp-1)
        if temp*2<100001 and not check[temp*2]:
            queue.append(temp*2)
    ans+=1