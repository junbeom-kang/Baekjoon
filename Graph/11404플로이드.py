import sys
input=sys.stdin.readline
INF=sys.maxsize
n=int(input())
m=int(input())
#배열을 INF로 초기화
arr=[[INF]*(n+1) for _ in range(n+1)]
#각 노선의 최솟값들을 입력받는다
for i in range(m):
    x,y,z=list(map(int,input().split()))
    if z<arr[x][y]:
        arr[x][y]=z
#플로이드 알고리즘
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            #출발점과 도착점이 같은경우는 없으므로
            if i==j:
                arr[i][j]=0
                continue
            arr[i][j]=min(arr[i][k]+arr[k][j],arr[i][j])
#정답 출력
for i in range(1,n+1):
    for j in range(1,n+1):
        if arr[i][j]==INF:
            print(0,end=' ')
        else:
            print(arr[i][j],end=' ')
    print()