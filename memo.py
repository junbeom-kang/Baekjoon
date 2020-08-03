import sys
input=sys.stdin.readline
n=int(input())
stack=[]
for i in range(n):
    a,b=input().split()
    a=int(a)
    stack.append([a,b])
for i in sorted(stack,key=lambda x:x[0]):
    print(*i)