import sys

def input():
    return sys.stdin.readline()
T=int(input())
for i in range(T):
    arr=[]
    stack=[]
    sum=0
    n=int(input())
    for j in range(n):
        p,q=map(int,input().split())
        arr.append((p,q))
    arr.sort()
    for m in arr:
        if m[1]<=arr[0][1]:
            stack.append(m)
    print(stack)
    stack=sorted(stack,key=lambda x:x[1])
    print(stack)
    for m in stack:
        if m[0]<=stack[0][0]:
            sum+=1
    print(sum)
