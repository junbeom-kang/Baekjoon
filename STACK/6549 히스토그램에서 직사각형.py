import sys
input=sys.stdin.readline

def solve(temp):
    ans=0
    stack=[(temp[1],0)]
    for i,high in enumerate(temp[2:],1):
        if high>=stack[-1][0]:
            stack.append((high,i))
        elif stack:
            while stack and stack[-1][0]>high:
                a,b=stack.pop()
                ans=max((i-b)*a,ans)
            stack.append((high,i))
    while stack:
        a,b=stack.pop()
        ans=max((temp[0]-b)*a,ans)
    return ans
while 1:
    temp=list(map(int,input().split()))
    if temp[0]==0:
        break
    print(max(solve(temp),solve([temp[0]]+temp[1:][::-1])))
