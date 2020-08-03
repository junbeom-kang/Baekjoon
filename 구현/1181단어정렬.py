import sys
input=sys.stdin.readline
n=int(input())
stack=[[] for _ in range(50)]

for i in range(n):
    x=input().strip()
    stack[len(x)-1].append(x)
for i in stack:
    i=set(i)
    i=list(i)
    i.sort()
    for j in i:
        print(j,end='')
        print()
