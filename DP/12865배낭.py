import sys
input=sys.stdin.readline
n,k=map(int,input().split())
stack=[[]]


for i in range(n):
    stack.append(list(map(int,input().split())))
adj=[[0 for i in range(k+1)]for _ in range(n+1)]


for i in range(1,n+1):
    for j in range(1,k+1):
        if stack[i][0]>j:
            adj[i][j]=adj[i-1][j]
        else:
            adj[i][j]=max(adj[i-1][j],adj[i-1][j-stack[i][0]]+stack[i][1])
print(adj[-1][-1])

