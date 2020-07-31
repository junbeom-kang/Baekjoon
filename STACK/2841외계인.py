import sys
def input():
    return sys.stdin.readline()
n,p=map(int,input().split())
data=[[]for _ in range(n)]
for i in range(n):
    data[i]=(list(map(int,input().split())))
stack=[[]for _ in range(7)]
count=0
for i in data:
    if not stack[i[0]]:
        stack[i[0]].append(i[1])
        count+=1
    elif i[1]>stack[i[0]][-1]:
        stack[i[0]].append(i[1])
        count+=1
    elif i[1]==stack[i[0]][-1]:
        continue
    elif i[1]<stack[i[0]][-1]:
        while stack[i[0]] and i[1]<stack[i[0]][-1]:
            stack[i[0]].pop()
            count+=1
        if stack[i[0]] and stack[i[0]][-1]==i[1]:
            continue
        stack[i[0]].append(i[1])
        count+=1
print(count)

