import sys
from collections import deque
def input():
    return sys.stdin.readline()
T=int(input())
for i in range(T):
    n,q=list(map(int,input().split()))
    cnt=0
    stack=list(map(int,input().split()))
    high=sorted(stack)
    queue=deque()
    for i in range(n):
        queue.append(i)
    while True:
        if high[-1]==stack[queue[0]]:
            high.pop()
            temp=queue.popleft()
            cnt+=1
            if temp==q:
                print(cnt)
                break
        else:
            queue.append(queue.popleft())
