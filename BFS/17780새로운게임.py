import sys
input=sys.stdin.readline


def solution(arr,index,n):
    cnt=0
    can=False
    while cnt<1001:
        for i in range(k):
            if where[index[i][0]][index[i][1]]:
                if where[index[i][0]][index[i][1]][0] == i:
                    t=index[i][2]
                    nx=index[i][0]+dx[t]
                    ny=index[i][1]+dy[t]
                    if 0<=nx<n and 0<=ny<n and arr[nx][ny]!=2:
                        if arr[nx][ny]==1:
                            where[nx][ny].extend(where[index[i][0]][index[i][1]][::-1])
                            where[index[i][0]][index[i][1]]=[]
                        else:
                            where[nx][ny].extend(where[index[i][0]][index[i][1]])
                            where[index[i][0]][index[i][1]] = []
                        for t in where[nx][ny]:
                            index[t][0]=nx
                            index[t][1]=ny
                    else:
                        if index[i][2]==1:
                            index[i][2]=2
                        elif index[i][2]==2:
                            index[i][2]=1
                        elif index[i][2]==3:
                            index[i][2]=4
                        else: index[i][2]=3
                        tt = index[i][2]
                        nx = index[i][0] + dx[tt]
                        ny = index[i][1] + dy[tt]
                        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 2:
                            if arr[nx][ny] == 1:
                                where[nx][ny].extend(where[index[i][0]][index[i][1]][::-1])
                                where[index[i][0]][index[i][1]] = []
                            else:
                                where[nx][ny].extend(where[index[i][0]][index[i][1]])
                                where[index[i][0]][index[i][1]] = []
                            for t in where[nx][ny]:
                                index[t][0] = nx
                                index[t][1] = ny
        cnt+=1
        for a,b,c in index:
            if len(where[a][b])>=4:
                can=True
                break
        if can:
            break
    if can:
        print(cnt)
    else:
        print(-1)






if __name__ == '__main__':
    dx = [0,0, 0, -1, 1]
    dy = [0,1, -1, 0, 0]
    n,k=map(int,input().split())
    arr=[]
    index=[]
    for i in range(n):
        arr.append(list(map(int,input().split())))
    for i in range(k):
        temp=list(map(int,input().split()))
        index.append([temp[0]-1,temp[1]-1,temp[2]])
    where=[[[] for _ in range(n)] for _ in range(n)]
    for z,(x,y,c) in enumerate(index):
        where[x][y].append(z)
    solution(arr,index,n)