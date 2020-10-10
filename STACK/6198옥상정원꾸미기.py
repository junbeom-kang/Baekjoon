import sys
input=sys.stdin.readline
n=int(input())
stack=[]
top=0
data=[]
ans=0
for _ in range(n):
    data.append(int(input()))
for i in range(n):
    if data[i]>=top:
        stack=[data[i]]
        top=data[i]
    elif data[i]>=stack[-1]:
        while data[i]>=stack[-1]:
            stack.pop()
        ans+=len(stack)
        stack.append(data[i])
    else:
        ans+=len(stack)
        stack.append(data[i])
print(ans)