import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
adj=[[]for _ in range(m+1)]
for i in range(m):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
invite=[]
invite.extend(adj[1])
for i in adj[1]:
    invite.extend(adj[i])
invite=set(invite)
print(len(invite)-1)