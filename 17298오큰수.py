import sys
n = int(sys.stdin.readline())
input = list(map(int, sys.stdin.readline().split()))
stack = []
result = [-1 for _ in range(n)]
stack.append(0)
for i in range(1,n):
    while stack and input[stack[-1]]<input[i]:
        result[stack.pop()]=input[i]
    stack.append(i)
for i in range(n):
    print(result[i],end=' ')