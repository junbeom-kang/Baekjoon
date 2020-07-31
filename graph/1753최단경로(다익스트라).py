import sys
INF=sys.maxsize

def input():
    return sys.stdin.readline()
#입력 받음.
v,e=map(int,input().split())
k=int(input())
adj=[[]for _ in range(v+1)]

for _ in range(e):
    u,v,w=map(int,input().split())
    adj[u].append([v,w])
ans=[INF]*(v+1)
for i in adj[k]:
    ans[i[0]]=i[1]
print(ans)

check=[False]*(v+1)
check[k]=True
#방문 하지 않은곳중에 가장 작은곳의 인덱스 반환
while True:
    temp=INF
    for i in range(1,v+1):
        if not check[i] and ans[i]<temp:
            temp=ans[i]
            N=i
#만약 갈수있는곳이 없으면 그대로 출력후 종료
    if temp==INF:
        ans[k]=0
        for i in ans[1:]:
            if i==INF:
                print('INF')
            else:
                print(i)
        sys.exit()

    #방문처리
    check[N]=True
    #방문한곳에서 더 효율적인 경로가 있으면 교체
    for i in range(1,v+1):
        if check[i]:
            continue
        if ans[i]>ans[N]+adj[N][i]:
            adj[k][i]=adj[k][N]+adj[N][i]
