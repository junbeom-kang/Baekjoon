import sys
input=sys.stdin.readline
from collections import deque
n,a,b=list(map(int,input().split()))
duck=deque([[a-1,1],[b-1,1]])
where=[[]for _ in range(21)]
if a==b:
    print(0)
    sys.exit()
if (a % 2 and not b % 2) or (not a % 2 and b % 2):
    print('-1')
    sys.exit()

def bfs(duck):
    while duck:
        temp=duck.popleft()
        if temp[0]+2**(temp[1]-1)<=n-1:
            duck.append([temp[0]+2**(temp[1]-1),temp[1]+1])
            where[temp[1]].append(temp[0]+2**(temp[1]-1))
        if temp[0]-2**(temp[1]-1)>=0:
            duck.append([temp[0]-2**(temp[1]-1),temp[1]+1])
            where[temp[1]].append(temp[0]-2**(temp[1]-1))

bfs(duck)
for i in range(21):
    temp=set(where[i])
    if len(where[i])!=len(temp):
        print(i)
        sys.exit()
print('-1')