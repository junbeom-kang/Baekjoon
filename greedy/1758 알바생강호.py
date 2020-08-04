import sys

def input():
    return sys.stdin.readline()

n=int(input())
stack=[]
for i in range(n):
    stack.append(int(input()))
stack.sort(reverse=True)
sum=0
for i in range(n):
    if stack[i]-i<=0:
        break
    sum+=stack[i]-i
print(sum)