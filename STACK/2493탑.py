import sys
input=sys.stdin.readline
n=int(input())
adj=list(map(int,input().split()))
ans=[0]
high=0
stack=[0]
for i in range(1,n):
    if adj[i]>adj[high]:
        high=i
        ans.append(0)
        stack=[i]
    elif adj[i]>=adj[stack[-1]]:
        cnt=0
        while adj[i]>adj[stack[-1]]:
            stack.pop()
            cnt+=1
        ans.append(stack[-1]+1)
        stack.append(i)

    elif adj[stack[-1]]>adj[i]:
        stack.append(i)
        ans.append(stack[-1])
print(*ans)
