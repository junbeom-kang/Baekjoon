import sys
def input():
    return sys.stdin.readline()
n=int(input())
data=[[0]for _ in range(n)]
ans=0
for i in range(n):
    stack=[]
    data[i]=(list(input().strip()))
    for j in data[i]:
        if not stack:
            stack.append(j)
        else:
            if stack[-1]==j:
                stack.pop()
            else:
                stack.append(j)
    if not stack:
        ans+=1
print(ans)