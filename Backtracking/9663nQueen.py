import sys
n=int(sys.stdin.readline())
count=0
stack=[]
def DFS(num):
    global count
    stack.append(num)
    if len(stack)==n:
        count+=1
        return
    for i in range(n):
        can = True
        if i in stack:
            continue
        gap=len(stack)
        for m in stack:
            if m+gap==i or m-gap==i:
                can=False
                break
            gap-=1
        if can:
            DFS(i)
            stack.pop()
for i in range(n):
    DFS(i)
    stack.pop()

print(count)
