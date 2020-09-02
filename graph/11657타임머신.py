import sys
input = sys.stdin.readline
n,m=map(int,input().split())
INF=sys.maxsize

adj=[[]for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    adj[a].append((c,b))
def ford():
    ans = [INF] * (n + 1)
    ans[1] = 0
    for i in range(1,n):
        for j in range(1,n+1):
            for c,b in adj[j]:
                if ans[j]==INF:
                    continue
                if ans[b]>c+ans[j]:
                    ans[b]=c+ans[j]
    for j in range(1,n+1):
        for c,b in adj[j]:
            if ans[j]==INF:
                continue
            if ans[b]>ans[j]+c:
                print(-1)
                sys.exit()
    return ans

temp=ford() 
for i in range(2,n+1):
    if temp[i]==INF:
        print(-1)
    else:
        print(temp[i])
