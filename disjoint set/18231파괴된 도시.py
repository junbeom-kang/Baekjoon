import sys
input=sys.stdin.readline
n,m=map(int,input().split())
adj=[[]for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
k=int(input())
destroy=list(map(int,input().split()))
check=[0]*(n+1)
ans=[]
count=0
for i in destroy:
    check[i]=1

for i in destroy:
    avail = True
    for j in adj[i]:

        if check[j]==0:
            avail=False

            break
    if avail:
        ans.append(i)
        count+=1
anan=set()
for i in ans:
    anan.add(i)
    anan.update(adj[i])
if len(anan)<k:
    print('-1')
    sys.exit()
print(count)
for i in ans:
    print(i,end=' ')
print(*ans,)