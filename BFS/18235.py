from collections import deque
import sys
input=sys.stdin.readline

N,A,B=map(int,input().split())
five=deque([A-1])
six=deque([B-1])

def bfs(five,six):
    i=1
    cnt=1
    while five and six:
        visit=[0]*N
        for _ in range(len(five)):
            temp=five.popleft()
            if temp+i<=N-1:
                five.append(temp+i)
                visit[temp+i]=1
            if temp-i>=0:
                five.append(temp-i)
                visit[temp-i]=1
        for _ in range(len(six)):
            temp1=six.popleft()
            if temp1+i<=N-1:
                if visit[temp1+i]:
                    return cnt
                else:
                    six.append(temp1+i)
            if temp1-i>=0:
                if visit[temp1-i]:
                    return cnt
                else:
                    six.append(temp1-i)
        i*=2
        cnt+=1
    return -1
if A==B:
    print(0)
else:
    print(bfs(five,six))