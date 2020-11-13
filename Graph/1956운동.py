## adj[i][i]를 0으로 초기화 하지않고 순환값을 구할 수 있다.
import sys
input=sys.stdin.readline
v,e=map(int,input().split())
INF=sys.maxsize
adj=[[INF]*(v+1)for _ in range(v+1)]
for _ in range(e):
    a,b,c=map(int,input().split())
    adj[a][b]=c
for i in range(1,v+1):
    adj[i][i]=0
for k in range(1,v+1):
    for i in range(1,v+1):
        for j in range(1,v+1):
            adj[i][j]=min(adj[i][j],adj[i][k]+adj[k][j])
ans=INF

for i in range(1,v+1):
    for j in range(i,v+1):
        if i==j:
            continue
        else:
            ans=min(adj[i][j]+adj[j][i],ans)
if ans==INF:
    print(-1)
else:
    print(ans)
print(adj)
'''
result = INF
for i in range(1, V + 1):  # 돌아오는 사이클 중 가장 최소거리 찾기
    result = min(result, matrix[i][i])

if result == INF:
    print(-1)
else:
    print(result)
'''