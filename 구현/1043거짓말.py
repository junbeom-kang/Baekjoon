import sys
input=sys.stdin.readline
n,m=map(int,input().split())
know=list(map(int,input().split()))
if len(know)==1:
    print(m)

else:
    know = set(know[1:])
    adj=[[]for _ in range(m)]
    for i in range(m):
        adj[i]=set(list(map(int,input().split()))[1:])
    for _ in range(m):
        for i in range(m):
            for j in know:
                if j in adj[i]:
                    know=adj[i]|know
                    break
    ans=0
    for i in adj:
        can = True
        for j in know:
            if j in i:
                can=False
                break
        if can:
            ans+=1
    print(ans)



